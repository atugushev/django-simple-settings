#!/usr/bin/env python
import os
import sys

from django.conf import settings
from django.core.management import call_command


def runtests():
    if not settings.configured:
        # Choose database for settings
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        }
        # Configure test environment
        settings.configure(
            DATABASES = DATABASES,
            INSTALLED_APPS = (
                'simple_settings',
            ),
            ROOT_URLCONF = None,
            LANGUAGES = (
                ('en', 'English'),
            ),
        )

    failures = call_command(
        'test', 'simple_settings', interactive=False, failfast=False,
        verbosity=2)
    sys.exit(bool(failures))


if __name__ == '__main__':
    runtests()
