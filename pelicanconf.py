#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'JMLobato'
SITENAME = 'PruebaPelican'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('GitHub', 'https://github.com/JMLobato/JMLobato.github.io'),
		 ('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('GitHub', 'https://github.com/JMLobato/JMLobato.github.io'),)
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Specify theme
THEME = "/home/decanosuitai/pelican/tema/pelican-bootstrap3-lovers"
BOOTSTRAP_THEME = "lovers"
STATIC_PATHS = ['images']
HEADER_IMAGE = "cabecera.jpg"
PROFILE_PICTURE = "biohazard.png"
