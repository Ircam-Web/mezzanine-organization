# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-12-21 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization-magazine', '0019_auto_20170105_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamiccontentarticle',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dynamic_content_articles', to='organization-magazine.Article', verbose_name='article'),
        ),
    ]