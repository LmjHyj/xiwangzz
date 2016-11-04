# coding=utf-8

import sys
from .settings_base import *

DEBUG = False

ALLOWED_HOSTS = [
    '.xiwangzz.com',
]

DEFAULT_DB = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'xiwangzz',
    'HOST': 'localhost',
    'PORT': '3306',
    'USER': 'root',
    'PASSWORD': '123456',
}

DATABASES = {
    'default': DEFAULT_DB
}
