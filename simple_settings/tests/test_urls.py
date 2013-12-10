try:
    from django.conf.urls import url, patterns
except ImportError:  # for Django 1.3 support
    from django.conf.urls.defaults import url, patterns


from .test_views import test_context_processor

urlpatterns = patterns('', url(r'^test_context_processor/$', test_context_processor))