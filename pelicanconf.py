#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Victor Gau'
SITENAME = u'Victor Gau'
SITEURL = ""
#SITEURL = 'http://victorgau.github.io'

PATH = 'content'
TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('iPython','http://ipython.org/'),
         ('Flask','http://flask.pocoo.org/'),
         ('Django','https://www.djangoproject.com/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('PyCharm Guide','https://www.jetbrains.com/pycharm/quickstart/'),
         ('RStudio','https://www.rstudio.com/'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/victorgau'),)

DISPLAY_TAGS_INLINE = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
RELATIVE_URLS = False

THEME = "pelican-themes/pelican-bootstrap3"
DISQUS_SITENAME = 'victorgau'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook', 'tag_cloud']

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'