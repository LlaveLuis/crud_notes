#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.conf.urls import include, url

urlpatterns = [
    url(r'^posts/list', 'crud.views.posts', name='list_posts'),
    url(r'^posts/add/', 'crud.views.add_post', name='add_post'),
    url(r'^posts/(?P<postid>\d+)/', 'crud.views.update_post', name='update_post'),
    url(r'^posts/(?P<postid>\d+)/delete/', 'crud.views.delete_post',
        name='delete_post'),
]
