from django.conf.urls import url
from .views import *

app_name = 'transformators'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^pages/$', pages, name='pages'),
    url(r'^tests/$', tests, name='tests'),
    url(r'^pages/(?P<page_number>[0-9]+)/$', page, name='page'),
    url(r'^test/(?P<test_number>[0-9]+)/$', autoriz, name='autoriz'),
    url(r'^test/(?P<test_number>[0-9]+)/(?P<pupil_id>[0-9]+)/$', test, name='test'),
    url(r'^result/(?P<test_number>[0-9]+)/(?P<pupil_id>[0-9]+)/$', result, name='result'),
	url(r'^about/$', about, name='about'),
	url(r'^help/$', help, name='help'),
]
