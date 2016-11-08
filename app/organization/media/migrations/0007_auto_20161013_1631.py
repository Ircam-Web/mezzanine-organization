# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-13 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('organization-pages', '0008_auto_20161013_1631'),
        ('organization-magazine', '0012_auto_20161013_1631'),
        ('organization-media', '0006_auto_20161013_1631'),
        ('organization-network', '0038_auto_20161013_1631'),
        ('organization-projects', '0020_auto_20161013_1631'),
        ('organization-agenda', '0009_auto_20161013_1631'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Audio',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.AddField(
            model_name='playlistmedia',
            name='media',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='playlists', to='organization-media.Media', verbose_name='media'),
        ),
        migrations.AddField(
            model_name='playlistmedia',
            name='playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medias', to='organization-media.Playlist', verbose_name='playlist'),
        ),
        migrations.AddField(
            model_name='mediatranscoded',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transcoded', to='organization-media.Media', verbose_name='media'),
        ),
        migrations.AddField(
            model_name='media',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='medias', to='organization-media.MediaCategory', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='media',
            name='site',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]