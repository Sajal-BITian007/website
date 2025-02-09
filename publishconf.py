#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
#don't change anything unless you are 100% sure.
# This file is only used if you use `make publish` or
# explicitly specify it as your configure file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.krisyu.org'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = 'disqus-sitename'
#GOOGLE_ANALYTICS = 'google-analytics-id'
