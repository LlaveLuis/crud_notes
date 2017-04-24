#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import check_password


class User(models.Model):
    """Represents an application user."""
    username = models.CharField(max_length=32)
    passwd = models.CharField(max_length=128)
    real_name = models.CharField(max_length=128)
    level = models.ForeignKey('Level')
    last_access = models.DateTimeField(blank=True, null=True)
    creation_user = models.IntegerField()
    modify_user = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'user'

    def registry(self):
        """Registry successful user login."""
        self.last_access = timezone.now()
        self.save(force_update=True)
        return None


class Level(models.Model):
    """Represent an user's level.
    Used to show some characteristics to specific kind of user."""
    description = models.CharField(max_length=32)

    class Meta:
        db_table = 'level'


def verify_user(username, passwd):
    """Data received is used to check user existence in DB; in case exists,
    registry his access.
    :return: {id_user: id_user, name: real_name, user_name: user_level} if user
    exists,
             {id_user: None, name: None, user_level: None } if doesn't
    """
    res = {'id_user': None, 'name': None, 'user_type': None, }
    usr = User.objects.filter(username=username)
    if len(usr) > 0:
        if check_password(passwd, usr[0].passwd):
            usr[0].registry()
            res['id_user'] = usr[0].id
            res['name'] = usr[0].real_name
            res['user_type'] = usr[0].level
    return res


def registry_user(id_user):
    """Search user in DB, and register if exists
    :return: {name: real_name} if user exists, {name: None } if doesn't
    """
    res = {'name': None, }
    usr = User.objects.filter(id=id_user)
    if len(usr) > 0:
        usr[0].registry()
        res['name'] = usr[0].real_name
    return res
