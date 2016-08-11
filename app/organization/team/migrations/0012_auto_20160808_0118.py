# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-07 23:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization-core', '0010_auto_20160808_0118'),
        ('organization-team', '0011_auto_20160727_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL')),
            ],
            options={
                'verbose_name': 'person link',
            },
        ),
        migrations.RemoveField(
            model_name='link',
            name='link_type',
        ),
        migrations.RemoveField(
            model_name='link',
            name='person',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='url',
        ),
        migrations.AddField(
            model_name='organization',
            name='website',
            field=models.URLField(blank=True, max_length=512, verbose_name='website'),
        ),
        migrations.DeleteModel(
            name='Link',
        ),
        migrations.DeleteModel(
            name='LinkType',
        ),
        migrations.AddField(
            model_name='personlink',
            name='link_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization-core.LinkType', verbose_name='link type'),
        ),
        migrations.AddField(
            model_name='personlink',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization-team.Person', verbose_name='person'),
        ),
    ]