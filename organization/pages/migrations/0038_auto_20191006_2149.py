# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-10-06 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-pages', '0037_auto_20190527_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeimage',
            name='title',
            field=models.CharField(blank=True, default='', max_length=1024, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='homeimage',
            name='title_en',
            field=models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='pageblock',
            name='title',
            field=models.CharField(blank=True, default='', max_length=1024, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='pageblock',
            name='title_en',
            field=models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='pageimage',
            name='title',
            field=models.CharField(blank=True, default='', max_length=1024, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='pageimage',
            name='title_en',
            field=models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='title'),
        ),
    ]
