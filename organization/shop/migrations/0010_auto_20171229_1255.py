# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-12-29 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization-shop', '0009_auto_20161026_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlink',
            name='title_fr',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='content_fr',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='description_fr',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='title_fr',
        ),
    ]
