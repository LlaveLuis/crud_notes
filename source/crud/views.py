#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.contrib import messages

from .models import Post


def posts(request):
    """View to list existing posts"""
    return render_to_response("posts.html",
                              {"posts": Post.objects.all(),
                               "messages": messages.get_messages(request)}
                              )


def add_post(request):
    return None


def delete_post(request):
    return None


def update_post(request):
    return None
