# Don't change any of the below 👇 unless you've read the docs.
from pelican.utils import SafeDatetime

SITENAME = 'NSPS'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
PATH_METADATA = r"(?P<path_no_ext>.*)\..*"
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = "{path_no_ext}.html"

THEME="."
TIMEZONE="America/Vancouver"
DATE_FORMATS = {
    "en": "%a %d %b %Y &bull; %I:%M %p",
}

AUTHORS_SAVE_AS=""
ARCHIVES_SAVE_AS=""
CATEGORIES_SAVE_AS=""
TAGS_SAVE_AS=""
CATEGORY_SAVE_AS=""

TYPOGRIFY=True
ARTICLE_ORDER_BY="date"

THEME_TEMPLATES_OVERRIDES=["event"]

DEFAULT_PAGINATION = False
OUTPUT_PATH="docs"

# The default timezone.
from datetime import datetime
from zoneinfo import ZoneInfo
NOW = datetime.now(ZoneInfo("America/Vancouver"))

# Set the default date for any .md file, such as uploads.
DEFAULT_DATE='fs'

# Monkey patch in a processor for `photo` that converts to an integer for use in the template.
from pelican.readers import METADATA_PROCESSORS
METADATA_PROCESSORS["photos"] = lambda x, _y: int(x) if x else 0

# Configurable settings, feel free to change the ones below 👇👍

# These appear on the bottom left of the site.
# Format: URL, Title, Text
LINKS = [    
    ["https://www.martingodwyn.com/", "Landscape &amp; Nature Photographer", "Amor Lucis Photography"],
    ["https://www.beauphoto.com/", "Supplying photographers in the lower mainland and across Canada since 1982.", "Beau Photo Supplies"],
    ["https://www.capacanada.ca/", "Canadian Association for Photographic Art", "CAPA"],
    ["https://capacanada.ca/updated-ai-requirements-on-capa-competitions/", "The Canadian Association for Photographic Art updated Artificial Intelligence (AI) Requirements on CAPA Competitions", "CAPA: Updated AI Requirements"],
    ["https://grinkecreative.com/", "Len Grinke's Photography Workshops", "Len Grinke Photography"],
    ["https://www.londondrugs.com/", "", "London Drugs"],
    ["https://www.neilbennettphoto.ca/", "", "Neil Bennett Photography"],
]

# These appear on the bottom right of the site.
# Format: URL, Title, Text
CONTACTS = [
    ["mailto:webmaster@nsps.ca", "", "Email"],
    ["https://northshorepho-kj37343.slack.com/", "Members Only", "Slack"],
    ["https://www.facebook.com/North-Shore-Photographic-Society-185057961533431/", "", "Facebook"],
    ["https://bsky.app/profile/northshoreps.bsky.social", "", "Bluesky"],
]

# The carousel images.
# Images should be static/originals, the photos.yml job will create a compressed version.
# Format: image name (don't include the path), Title, Photographer
CAROUSEL = [
    ["20260706_A4_Sibling-Solidarity_Ruth-Campling_CMPYes_NSPYes_SOCYes_No-AIYes.jpg", "Sibling Solidarity", "Ruth Campling"],
    ["AND_9632.jpeg", "Osprey", "Andy McKay"],
    ["20260709_A3_Barn-Wood_Emogene-Emogene_CMPYes_NSPYes_SOCYes_No-AIYes.jpg", "Barn Wood", "Emogene"]
]

# Alters events to hide past events and limit the number of future events displayed.
PLUGINS = ["events"]
