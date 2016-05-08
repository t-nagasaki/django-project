"""
Django production settings for foo project.
"""

from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = [
    # ('Your Name', 'your_email@example.com'),
]

# Hosts/domain names that are valid for this site.
# See https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h_hejho&_ehn@ngg(8$$^*qh=z$welns&9%*@^s-*vla71b@da'
