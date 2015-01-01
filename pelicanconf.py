#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Leta Montopoli'
SITENAME = u'The L Blog'
SITEURL = 'http://lmontopo.github.io'
TIMEZONE = 'America/Detroit'
MD_EXTENSIONS = ['codehilite(css_class=highlight, linenums=True)','extra']
THEME = 'pelican-themes/zurb-F5-basic'


PATH = 'content'

DEFAULT_CATEGORY = 'Blog'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
TAG_FEED_ATOM = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
