#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'entry.views.access', name='home'),
]
