# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-19 11:53
from __future__ import unicode_literals

from django.db import migrations, models
from organization.network.models import Team


#def generate_slugs(apps, schema_editor):
#    teams = Team.objects.all()
#    for team in teams:
#        team.save()


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0117_merge_20181204_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='slug',
            field=models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the name.', max_length=2000, null=True, verbose_name='URL'),
        ),
    ]
