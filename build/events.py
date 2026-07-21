import requests
import icalendar
import datetime
import os
import sys
import argparse

calendar_url = "https://nsps.ca/?post_type=tribe_events&ical=1&eventDisplay=list"
root = os.path.abspath("content/event")
assert os.path.exists(root), f"The directory {root} doesn't exist."

def get_calendar():
    headers = {"User-Agent": "mod_security sucks"}
    r = requests.get(calendar_url, headers=headers)
    return icalendar.Calendar.from_ical(r.text)

def slugify(event):
    return event.DTSTART.strftime("%Y-%m-%d") + "-" + event.summary.lower().replace(' ', '-').replace(':', '')

def format_event(event):
    template = f"""Title: {event.summary}
Date: {event.DTSTART.strftime("%Y-%m-%d %H-%M")}
URL: /events/{event.slug}
Template: event
UID: {event.uid}

{event.description}
"""
    return template

def write_event(event):
    path = event.slug + ".md"
    abspath = os.path.join(root, path)
    if os.path.exists(abspath):
        with open(abspath, "r") as f:
            if f"UID: {event.uid}" not in f.read():
                raise(f"❌ Something already exists at {event.slug}.")
    
    exists = os.path.exists(abspath)
        
    with open(abspath, "w") as f:
        f.write(event.formatted)
        if exists:
            print(f"👍 Updating {event.slug}.")                
        else:
            print(f"✅ Added {event.slug}.")

def get_events_from_calendar():
    cal = get_calendar()
    for element in cal.walk():
        if isinstance(element, icalendar.cal.event.Event):
            element.slug = slugify(element)
            element.formatted = format_event(element)
            write_event(element)

if __name__=='__main__':
    get_events_from_calendar()