# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-19 13:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0118_team_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='url',
        ),
    ]