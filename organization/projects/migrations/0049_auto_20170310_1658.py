# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-03-10 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-projects', '0048_auto_20170307_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectictdata',
            name='validation_status',
        ),
        migrations.AddField(
            model_name='project',
            name='validation_status',
            field=models.IntegerField(choices=[(0, 'rejected'), (1, 'pending'), (2, 'in process'), (3, 'accepted')], default=1, verbose_name='validation status'),
        ),
    ]
