#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mario Danic'
SITENAME = u'6sync | Blog'
SITEURL = ''

PATH = 'content/'

STATIC_PATHS = ("css", "fonts", "img", "js")
DIRECT_TEMPLATES = ('index',)

THEME = "theme"
THEME_STATIC_DIR = ""

AUTHORS_SAVE_AS = False
AUTHOR_SAVE_AS = False
TAGS_SAVE_AS = False
TAG_SAVE_AS = False
SUMMARY_MAX_LENGTH = 100

DEFAULT_DATE_FORMAT = "%B %d, %Y"
TIMEZONE = 'Pacific/Auckland'
LOCALE = ('en_US',)

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
