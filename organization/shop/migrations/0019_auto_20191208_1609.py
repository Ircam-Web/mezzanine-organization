# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-12-08 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization-shop', '0018_auto_20191107_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productexternalshop',
            name='label_en',
        ),
        migrations.RemoveField(
            model_name='productkeyword',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='productlink',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='title_en',
        ),
    ]
