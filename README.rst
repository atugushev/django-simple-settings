=====
Django Simple Settings
=====

A very simple settings

Quick start
-----------

1. Run `pip install django-simple-settings` to install a package.

2. Add "simple_settings" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'simple_settings',
    )

3. Run `python manage.py migrate` to create the settings models.

4. Simple use:

Use in code
.. code-block:: python
    from simple_settings import settings
    if settings.get('is_feature_available') == '1':
        print "Let's use this feature!"

Use in template
.. code-block:: python
    TEMPLATE_CONTEXT_PROCESSORS = (
        '...',
        'simple_settings.context_processors.simple_settings',
    )

.. code-block:: html
    {% if simple_settings.is_feature_available %}Let's use this feature!{% endif %}