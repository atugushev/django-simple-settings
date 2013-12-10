#!/usr/bin/env python
import sys
import os

from django.conf import settings
from django.core.management import call_command

BASE_DIR = os.path.dirname(__file__)


def runtests():
    if not settings.configured:
        # Configure test environment
        settings.configure(
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:'
                }
            },
            INSTALLED_APPS=(
                'simple_settings',
            ),
            TEMPLATE_CONTEXT_PROCESSORS = (
                'django.core.context_processors.request',
                'simple_settings.context_processors.simple_settings',
            ),
            TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'simple_settings'),),
            ROOT_URLCONF = 'simple_settings.tests.test_urls',
            LANGUAGES = (
                ('en', 'English'),
            ),
        )

    failures = call_command('test', 'simple_settings', interactive=False, failfast=False, verbosity=2)
    sys.exit(bool(failures))


if __name__ == '__main__':
    runtests()
