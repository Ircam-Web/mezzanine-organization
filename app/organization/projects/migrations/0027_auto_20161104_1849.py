# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-04 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization-projects', '0026_dynamiccontentproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectRelatedTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1024, null=True, verbose_name='title')),
                ('project', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_title', to='organization-projects.Project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'related title',
            },
        ),
        migrations.AlterOrderWithRespectTo(
            name='projectrelatedtitle',
            order_with_respect_to='project',
        ),
    ]
