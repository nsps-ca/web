from pelican.generators import ArticlesGenerator
from pelican import signals
import datetime

today = datetime.datetime.today()
counter = 0
MAX_NUMBER_EVENTS = 5

def event_parse(context, metadata):
    if metadata["template"] == "event":
        if metadata["date"] < today:
            metadata["status"] = "hidden"
            print(f"Event is in the past, hiding: {metadata['title']}")

        if metadata["date"] > today:
            global counter
            counter += 1
            if counter > MAX_NUMBER_EVENTS:
                metadata["status"] = "hidden"
                print(f"Event is in the future, but hiding more than 5 events: {metadata['title']}")

def register():
    signals.article_generator_context.connect(event_parse)