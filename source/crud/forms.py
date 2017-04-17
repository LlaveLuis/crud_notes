#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.forms import ModelForm, TextInput, Textarea
from django.forms.extras.widgets import SelectDateWidget

from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'date_pub', ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'size': 36, }),
            'content': Textarea(attrs={'class': 'form-control', 'rows': 4, }),
            'date_pub': SelectDateWidget(empty_label=('Choose Year',
                                                      'Choose Month',
                                                      'Choose Day')
                                         )
        }
