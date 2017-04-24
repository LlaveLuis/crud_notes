# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'level',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('username', models.CharField(max_length=32)),
                ('passwd', models.CharField(max_length=128)),
                ('real_name', models.CharField(max_length=128)),
                ('last_access', models.DateTimeField(null=True, blank=True)),
                ('creation_user', models.IntegerField()),
                ('modify_user', models.IntegerField(null=True, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modify_date', models.DateTimeField(null=True, blank=True)),
                ('level', models.ForeignKey(to='entry.Level')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
