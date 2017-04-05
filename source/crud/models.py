#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.db import models


class Post(models.Model):
    """Represents a redacted post"""
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_pub = models.DateTimeField()
