# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-10-17 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-projects', '0043_auto_20170130_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_archive',
            field=models.BooleanField(default=False, help_text='Hide project in Team Page', verbose_name='Is Archive'),
        ),
    ]