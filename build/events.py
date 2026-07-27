import requests
import icalendar
import datetime
import os
import glob
import sys
import argparse
from pelican.readers import MarkdownReader
from pelican.settings import read_settings

calendar_url = "https://nsps.ca/?post_type=tribe_events&ical=1&eventDisplay=list"
root = os.path.abspath("content/event")
assert os.path.exists(root), f"The directory {root} doesn't exist."
settings = read_settings()

def get_existing_events():
    """
    The slug of the event is based on the title and DTSTART,
    so this slug will be set when the event is first read. If those values
    get changed by a user afterwards, we don't want to generate a whole new
    slug, but instead find the existing one.

    This loops through all the events and finds the existing slug to reference.
    """
    events = {}
    reader = MarkdownReader(settings=settings)

    for path in glob.glob(root + "/*.md"):
        with open(path, "r") as f:
            md = reader.read(path)[1]
            events[md["uid"]] = md["slug"]

    return events

existing_events = get_existing_events()

def get_calendar():
    headers = {"User-Agent": "mod_security sucks"}
    r = requests.get(calendar_url, headers=headers)
    return icalendar.Calendar.from_ical(r.text)

def slugify(event):
    return event.DTSTART.strftime("%Y-%m-%d") + "-" + event.summary.lower().replace(' ', '-').replace(':', '')

def format_event(event):
    template = f"""Title: {event.summary}
Date: {event.DTSTART.strftime("%Y-%m-%d %H:%M")}
Slug: {event.slug}
Template: event
UID: {event.uid}

{event.description}
"""
    return template

def write_event(event):
    path = event.slug + ".md"
    abspath = os.path.join(root, path)
    exists = os.path.exists(abspath)

    with open(abspath, "w") as f:
        f.write(event.formatted)
        print(f"👍 Updating {event.slug}." if exists else f"✅ Added {event.slug}.")

def get_events_from_calendar():
    cal = get_calendar()
    for element in cal.walk():
        if isinstance(element, icalendar.cal.event.Event):
            element.slug = existing_events[element.uid] if element.uid in existing_events else slugify(element)
            element.formatted = format_event(element)
            write_event(element)

if __name__=='__main__':
    get_events_from_calendar()