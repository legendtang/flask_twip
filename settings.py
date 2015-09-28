#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import unicode_literals,\
    absolute_import, division, print_function
import os

TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
DEBUG = True
SECRET_KEY = str('')
