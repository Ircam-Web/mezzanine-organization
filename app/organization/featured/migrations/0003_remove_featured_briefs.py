# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization-featured', '0002_remove_featured_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featured',
            name='briefs',
        ),
    ]