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

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('IPython','http://ipython.org/'),
         ('Pandas','http://pandas.pydata.org/'),
         ('matplotlib','http://matplotlib.org/'),
         ('Scikit-Learn','http://scikit-learn.org/stable/'),
         ('Statsmodel','http://statsmodels.sourceforge.net/'),
         ('Django','https://www.djangoproject.com/'),
         ('Flask','http://flask.pocoo.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('nltk','http://www.nltk.org/'),
         ('jieba','https://github.com/fxsjy/jieba'),
         ('gensim','https://radimrehurek.com/gensim/'),
         ('PyCharm Guide','https://www.jetbrains.com/pycharm/quickstart/'),
         ('RStudio','https://www.rstudio.com/'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/victorgau'),
          ('BitBucket', 'https://bitbucket.org/victorgau'),)

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
           'liquid_tags.include_code', 'liquid_tags.notebook', 'tag_cloud', 'tipue_search']

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

BANNER = 'images/free_banner_red.jpg'
BANNER_SUBTITLE = 'Just Do It!'

ABOUT_ME = u"""突然發現自己對於股票投機的興趣，到了不做不可的程度，所以弄一個網站來記錄一些心得。"""
AVATAR = 'images/victor.jpg'