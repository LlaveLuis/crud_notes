#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.contrib import messages

from .models import Post
from .forms import PostForm


def posts(request):
    """View to list existing posts"""
    return render_to_response("posts.html",
                              {"posts": Post.objects.all(),
                               "messages": messages.get_messages(request)}
                              )


def add_post(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "The post has been saved!")
            return HttpResponseRedirect("/posts/list/")
    return render(request, 'form.html', {'form': form})


def delete_post(request):
    return None


def update_post(request):
    return None
