# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-04-18 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-projects', '0057_auto_20170412_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttopic',
            name='key',
            field=models.CharField(default='unknown', max_length=128, unique=True, verbose_name='key'),
        ),
    ]
