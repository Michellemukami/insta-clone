# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-01 15:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0012_profile_profile_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_id',
        ),
    ]
