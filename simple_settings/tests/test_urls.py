from django.conf.urls import patterns, url

from .test_views import test_context_processor

urlpatterns = patterns('', url(r'^test_context_processor/$', test_context_processor))