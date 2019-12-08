# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-30 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-media', '0019_merge_20190123_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaimage',
            name='type',
            field=models.CharField(choices=[('logo', 'logo'), ('logo_white', 'logo white'), ('logo_black', 'logo black'), ('logo_header', 'logo header'), ('logo_back', 'logo back'), ('logo_footer', 'logo footer'), ('slider', 'slider'), ('card', 'card'), ('page_slider', 'page - slider'), ('page_featured', 'page - featured')], max_length=64, verbose_name='type'),
        ),
    ]
