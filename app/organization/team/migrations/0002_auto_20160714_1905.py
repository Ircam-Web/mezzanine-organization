# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 17:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization-team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='_meta_title',
        ),
        migrations.RemoveField(
            model_name='person',
            name='created',
        ),
        migrations.RemoveField(
            model_name='person',
            name='description',
        ),
        migrations.RemoveField(
            model_name='person',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='person',
            name='gen_description',
        ),
        migrations.RemoveField(
            model_name='person',
            name='in_sitemap',
        ),
        migrations.RemoveField(
            model_name='person',
            name='keywords_string',
        ),
        migrations.RemoveField(
            model_name='person',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='person',
            name='short_url',
        ),
        migrations.RemoveField(
            model_name='person',
            name='site',
        ),
        migrations.RemoveField(
            model_name='person',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='person',
            name='status',
        ),
        migrations.RemoveField(
            model_name='person',
            name='title',
        ),
        migrations.RemoveField(
            model_name='person',
            name='updated',
        ),
    ]