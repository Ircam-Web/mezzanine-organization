# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-team', '0005_remove_person_nationality'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='is_on_map',
            field=models.BooleanField(default=True, verbose_name='is on map'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='birthday'),
        ),
    ]
