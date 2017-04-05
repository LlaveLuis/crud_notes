#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.forms import ModelForm
from models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'date_pub', ]
