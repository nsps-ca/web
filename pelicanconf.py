SITENAME = 'NSPS'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
PATH_METADATA = r"(?P<path_no_ext>.*)\..*"
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = "{path_no_ext}.html"

THEME="."

DATE_FORMATS = {
    "en": "%a %d %b %Y &bull; %H:%M %p",
}

AUTHORS_SAVE_AS=""
ARCHIVES_SAVE_AS=""
CATEGORIES_SAVE_AS=""
TAGS_SAVE_AS=""
CATEGORY_SAVE_AS=""

THEME_TEMPLATES_OVERRIDES=["event"]

DEFAULT_PAGINATION = False
OUTPUT_PATH="docs"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
