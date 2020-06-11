#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os


########################### General Settings ###################################
AUTHOR = u'Michael Oduor'
SITENAME = u'MattersEarthly'
# SITESUBTITLE = ''
# Base URL of the web site. 
SITEURL = ''

TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = u'en'

# CC_LICENSE = "CC-BY-NC-SA"

# Where to output the generated files.
OUTPUT_PATH = 'output/'

# Path to content directory to be processed by Pelican
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']

# Delete the output directory, and all of its contents, before generating new files. 
# This can be useful in preventing older, unnecessary files from persisting in your output.
DELETE_OUTPUT_DIRECTORY = True

################## Custom CSS #########################
CUSTOM_CSS = 'static/custom.css'
CUSTOM_JS = 'static/custom.js'

STATIC_PATHS = [ 'images', '../CNAME', 'extra/custom.css', 'extra/custom.js', 'extra/robots.txt' ]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/custom.js': {'path': 'static/custom.js'},
    'extra/robots.txt': {'path': 'robots.txt'},
    '../CNAME': {'path': 'CNAME'}
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/oduorm'),
          ('LinkedIn', 'https://www.linkedin.com/in/michaeloduor/'),
          ('GitHub', 'https://github.com/Modago'),
          ('GitLab', 'https://gitlab.fabcloud.org/academany/fabacademy/2019/labs/oulu/students/michael-oduor'),)

#TWITTER_CARDS = True

DEFAULT_PAGINATION = 5


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


############################ Plugins ######################################
PLUGIN_PATHS = ['plugins']

PLUGINS = ['i18n_subsites', 'liquid_tags.img', 
           'liquid_tags.video',  'liquid_tags.include_code',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'series']

'''
'tag_cloud',
'pelican_youtube',
'''

# for Tique Search Plugin
DIRECT_TEMPLATES = ('index','tags', 'categories', 'authors', 'archives', 'search')

# The maximum number of articles to include on a page, not including orphans. 
# False to disable pagination.
DEFAULT_PAGINATION = 5


JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}

I18N_TEMPLATES_LANG = 'en'

####################### Theme-Specific Settings #########################   
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly' #cosmo, simplex, sandstone, lumen,flatly

# SITELOGO = 'images/'
# SITELOGO_SIZE = ...
# FAVICON = 'images/extra'

BANNER = 'images/banner.jpg'

# BOOTSTRAP_NAVBAR_INVERSE = True

# Whether to display categories on the menu of the template. Templates may or not honor this setting.
DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_PAGES_ON_MENU = True

ARTICLE_EXCLUDES = ['extra']

# The URL to refer to an article.
ARTICLE_URL = 'articles/{slug}.html'

#The place where we will save an article.
ARTICLE_SAVE_AS = 'articles/{slug}.html'

#The URL we will use to link to a page.
PAGE_URL = '{slug}.html'

#The location we will save the page. 
#This value has to be the same as PAGE_URL or you need to use a rewrite in your server config.
PAGE_SAVE_AS = '{slug}.html'

# The URL to use for a tag.
TAG_URL = 'tags/{slug}.html'

#The location to save the tag page.
TAG_SAVE_AS = 'tags/{slug}.html'

#The location to save the tag list.
TAGS_URL = 'tags.html'

# Generate archive
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Order archives by newest first by date. (False: orders by date with older articles first.)
NEWEST_FIRST_ARCHIVES = True

# When creating a short summary of an article, this will be the default length (measured in words) of the text created. 
SUMMARY_MAX_LENGTH = 100

# DISPLAY_TAGS_INLINE = True

# RECENT_POST_COUNT = 5
# DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
# A list of glob patterns.
IGNORE_FILES = ['.#*', '__pycache__']


# If set to True, several typographical improvements will be incorporated into the generated HTML
TYPOGRIFY = True

HIDE_SIDEBAR = True

# Specifies where you want the slug to be automatically generated from.
# Can be set to title to use the ‘Title:’ metadata tag or basename to use the article’s file name when creating the slug
SLUGIFY_SOURCE = 'title'

# If disabled, content with dates in the future will get a default status of draft.
WITH_FUTURE_DATES = True
