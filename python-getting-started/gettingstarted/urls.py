from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^names/', hello.views.names, name='names'),
    url(r'^flagged/', hello.views.flagged, name='flagged'),
    url(r'^contact/', hello.views.contact, name='contact'),
]
