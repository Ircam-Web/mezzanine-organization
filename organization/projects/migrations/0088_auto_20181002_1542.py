# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-10-02 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-projects', '0087_auto_20180913_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcallimage',
            name='type',
            field=models.CharField(choices=[('logo', 'logo'), ('logo_white', 'logo white'), ('logo_black', 'logo black'), ('logo_header', 'logo header'), ('logo_footer', 'logo footer'), ('slider', 'slider'), ('card', 'card'), ('page_slider', 'page - slider'), ('page_featured', 'page - featured'), ('hero', 'hero')], max_length=64, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='projectcollectionimage',
            name='type',
            field=models.CharField(choices=[('logo', 'logo'), ('logo_white', 'logo white'), ('logo_black', 'logo black'), ('logo_header', 'logo header'), ('logo_footer', 'logo footer'), ('slider', 'slider'), ('card', 'card'), ('page_slider', 'page - slider'), ('page_featured', 'page - featured'), ('hero', 'hero')], max_length=64, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='type',
            field=models.CharField(choices=[('logo', 'logo'), ('logo_white', 'logo white'), ('logo_black', 'logo black'), ('logo_header', 'logo header'), ('logo_footer', 'logo footer'), ('slider', 'slider'), ('card', 'card'), ('page_slider', 'page - slider'), ('page_featured', 'page - featured'), ('hero', 'hero')], max_length=64, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='projectresidencyimage',
            name='type',
            field=models.CharField(choices=[('logo', 'logo'), ('logo_white', 'logo white'), ('logo_black', 'logo black'), ('logo_header', 'logo header'), ('logo_footer', 'logo footer'), ('slider', 'slider'), ('card', 'card'), ('page_slider', 'page - slider'), ('page_featured', 'page - featured'), ('hero', 'hero')], max_length=64, verbose_name='type'),
        ),
    ]