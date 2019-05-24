# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-24 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-agenda', '0031_auto_20180108_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventblock',
            name='content_fr',
        ),
        migrations.RemoveField(
            model_name='eventblock',
            name='description_fr',
        ),
        migrations.RemoveField(
            model_name='eventblock',
            name='title_fr',
        ),
        migrations.RemoveField(
            model_name='eventlink',
            name='title_fr',
        ),
        migrations.RemoveField(
            model_name='eventpricedescription',
            name='description_fr',
        ),
        migrations.RemoveField(
            model_name='eventpublictype',
            name='name_fr',
        ),
        migrations.RemoveField(
            model_name='eventrelatedtitle',
            name='title_fr',
        ),
        migrations.RemoveField(
            model_name='eventtraininglevel',
            name='name_fr',
        ),
        migrations.AlterField(
            model_name='eventtraining',
            name='language',
            field=models.CharField(blank=True, choices=[('en', 'English')], max_length=64, null=True, verbose_name='language'),
        ),
    ]