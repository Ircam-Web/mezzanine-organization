# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-25 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-magazine', '0006_auto_20160825_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='articles',
        ),
        migrations.AddField(
            model_name='article',
            name='topics',
            field=models.ManyToManyField(blank=True, null=True, related_name='articles', to='organization-magazine.Topic', verbose_name='topics'),
        ),
    ]