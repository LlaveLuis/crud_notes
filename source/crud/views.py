#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Post, User
from .forms import PostForm


def posts(request):
    """View to list existing posts"""
    if request.session.get('id_user') is None:
        request.session['res'] = 'Warn'
        messages.add_message(request, messages.WARNING,
                             "The session has expired")
        return HttpResponseRedirect(reverse('home'))
    return render(request, "posts.html",
                  {"posts": Post.objects.all().order_by('date_pub'),
                   "messages": messages.get_messages(request),
                   "users": User.objects.all().order_by('real_name')},
                  )


def add_post(request):
    """View to add a post"""
    if request.session.get('id_user') is None:
        request.session['res'] = 'Warn'
        messages.add_message(request, messages.WARNING,
                             "The session has expired")
        return HttpResponseRedirect(reverse('home'))
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.save(commit=False)
            data.author = User.objects.filter(id=request.session.get(
                'id_user'))[0]
            data.save()
            messages.add_message(request, messages.SUCCESS,
                                 "The post has been saved!")
            return HttpResponseRedirect("/posts/list/")
    return render(request, 'form.html', {'form': form})


def delete_post(request, postid):
    """View to delete a post, referenced by postid parameter"""
    if request.session.get('id_user') is None:
        request.session['res'] = 'Warn'
        messages.add_message(request, messages.WARNING,
                             "The session has expired")
        return HttpResponseRedirect(reverse('home'))
    instance = get_object_or_404(Post, id=postid)
    instance.delete()
    messages.add_message(request, messages.SUCCESS,
                         "The post with id %s has been deleted!" % postid)
    return HttpResponseRedirect(reverse('list_posts'))


def update_post(request, postid):
    """View to update an existing post, referenced by postid parameter.
    Reference to the same form used in add_post view."""
    if request.session.get('id_user') is None:
        request.session['res'] = 'Warn'
        messages.add_message(request, messages.WARNING,
                             "The session has expired")
        return HttpResponseRedirect(reverse('home'))
    instance = get_object_or_404(Post, id=postid)
    form = PostForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "The post has been updated!")
            return HttpResponseRedirect(reverse('list_posts'))
    return render(request, 'form.html', {'form': form})


def filter_posts(request):
    """List existing posts, filtering by user"""
    if request.is_ajax():
        id_user = int(request.POST.get('id_user'))
        if id_user>0:
            return render(request, "posts_list.html",
                          {"posts": Post.objects.filter(
                              author_id=id_user).order_by('date_pub'),
                           })
        else:
            return render(request, "posts_list.html",
                          {"posts": Post.objects.all().order_by('date_pub'),
                           })
    return None
