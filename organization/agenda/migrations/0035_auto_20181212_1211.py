# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-12 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization-agenda', '0034_merge_20181116_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventimage',
            name='credits_fr',
        ),
        migrations.RemoveField(
            model_name='eventimage',
            name='title_fr',
        ),
    ]
