# -*- coding: utf-8 -*-

import datetime
import os
from django.conf import global_settings
from django.contrib.messages import constants as messages

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    (u'Burak Sahin', 'buraksahin.tr@gmail.com'),
)

MANAGERS = ADMINS
TIME_ZONE = 'Europe/Istanbul'
LANGUAGE_CODE = 'tr-TR'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
SECRET_KEY = '^i1y1oz9fqn(q^t_0gs9ts9%hj3b2m*a40t)z9@@iy_j3#pn!)'
WSGI_APPLICATION = 'chapullmarket.wsgi.application'


PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale'),
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_ROOT = ''
MEDIA_URL = '/media/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, ''),
)

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

ROOT_URLCONF = 'chapullmarket.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'chapullmarket',
        'USER': 'chapullmarket',
        'PASSWORD': 'chapullmarket',
        'HOST': 'localhost',
        'PORT': '',
    },
}

TEMPLATE_DIRS = ()
for root, dirs, files in os.walk(PROJECT_PATH):
    if 'templates' in dirs:
        TEMPLATE_DIRS += (os.path.join(root, 'templates'),)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # this is default
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
