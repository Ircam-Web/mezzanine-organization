# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-01-09 10:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0139_auto_20200109_0853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personprofessionalcategory',
            options={'verbose_name': 'Professionnal category', 'verbose_name_plural': 'Professionnal categories'},
        ),
    ]
