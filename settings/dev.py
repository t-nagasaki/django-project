"""
Django development settings for foo project.
"""

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = [
    # ('Your Name', 'your_email@example.com'),
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h_hejho&_ehn@ngg(8$$^*qh=z$welns&9%*@^s-*vla71b@da'

# Add django-debug-toolbar in dev.
MIDDLEWARE_CLASSES += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INSTALLED_APPS += [
    'debug_toolbar',
]
INTERNAL_IPS = [
    '127.0.0.1',
]
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
DEBUG_TOOLBAR_PATCH_SETTINGS = False
