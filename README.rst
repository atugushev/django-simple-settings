=====
Django Simple Settings
=====

A very simple settings.

Quick start
-----------

1. Install a package.

.. code-block:: bash

    $ pip install django-simple-settings

2. Add "simple_settings" to your INSTALLED_APPS setting:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'simple_settings',
    )

2. Add context processor if you would like:

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS = (
        '...',
        'simple_settings.context_processors.simple_settings',
    )

3. Create models:

.. code-block:: bash

    $ python manage.py migrate

4. Simple use:

.. code-block:: python

    from simple_settings import settings
    if settings.get('is_feature_available'):
        print "Let's use this feature!"
    print settings.get('my_setting')
    print settings.get['my_setting']

.. code-block:: html+django

    {% if simple_settings.is_feature_available %}Let's use this feature!{% endif %}
    {{ simple_settings.is_feature_available }}
