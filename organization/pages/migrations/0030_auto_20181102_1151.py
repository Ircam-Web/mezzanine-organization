# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-02 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-pages', '0029_auto_20180529_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeimage',
            name='credits_en',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='credits'),
        ),
        migrations.AddField(
            model_name='homeimage',
            name='credits_fr',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='credits'),
        ),
        migrations.AddField(
            model_name='homeimage',
            name='title_en',
            field=models.CharField(max_length=1024, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='homeimage',
            name='title_fr',
            field=models.CharField(max_length=1024, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='pageimage',
            name='credits_en',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='credits'),
        ),
        migrations.AddField(
            model_name='pageimage',
            name='credits_fr',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='credits'),
        ),
    ]
