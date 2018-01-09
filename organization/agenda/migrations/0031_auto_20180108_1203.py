# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-01-08 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-agenda', '0030_auto_20171222_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtraining',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('fr', 'French')], max_length=64, null=True, verbose_name='language'),
        ),
    ]
