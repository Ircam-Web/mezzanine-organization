# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-06-01 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        #('skosxl', '0001_initial'),
        ('organization-projects', '0072_auto_20180307_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='concepts',
            field=models.IntegerField(),
        ),
    ]
