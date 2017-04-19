#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .forms import UserForm
from .models import verify_user, registry_user


def access(request):
    """View to process authentication user."""
    # verify if an open session exists
    id_server = request.session.session_key
    if id_server is not None:
        id_client = request.COOKIES['sessionid']
        id_user = request.session.get('id_user')
        if id_client == id_server and id_user:
            res = registry_user(id_user)
            if len(res) > 0:
                return HttpResponseRedirect('posts/list')
    # from POST, data verification is required
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            res = verify_user(request.POST['username'],
                              request.POST['passwd'])
            if len(res) > 0:
                request.session.create()
                if not ('remember' in request.POST):
                    request.session.set_expiry(300)
                request.session['id_user'] = res['id_user']
                request.session['name'] = res['name']
                return HttpResponseRedirect('posts/list')
        request.session['res'] = 'Err'
        messages.error(request, 'Wrong username or password')
        return redirect('home')
    else:
        return render(request, 'login.html')


def leave(request):
    """View for session close."""
    request.session.flush()
    return render(request, 'logout.html')
