# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-20 08:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization-projects', '0092_auto_20200703_1644'),
        ('organization-network', '0145_teamprojectordering'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='teamprojectordering',
            unique_together=set([('project_page', 'team_page')]),
        ),
    ]