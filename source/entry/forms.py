#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.forms import ModelForm

from .models import User


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'passwd']
