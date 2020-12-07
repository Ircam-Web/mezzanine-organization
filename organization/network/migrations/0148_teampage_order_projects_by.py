# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-29 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0147_auto_20200720_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='teampage',
            name='order_projects_by',
            field=models.CharField(choices=[('creation_date', 'Creation Date'), ('manual', 'Manuel')], default='creation_date', max_length=16, verbose_name='Projects ordering'),
            preserve_default=False,
        ),
    ]