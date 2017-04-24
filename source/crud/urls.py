#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^/list/filter/', 'crud.views.filter_posts', name='filter_posts'),
    url(r'^/list', 'crud.views.posts', name='list_posts'),
    url(r'^/add/', 'crud.views.add_post', name='add_post'),
    url(r'^/(?P<postid>\d+)/delete/', 'crud.views.delete_post',
        name='delete_post'),
    url(r'^/(?P<postid>\d+)/', 'crud.views.update_post', name='update_post'),
]
