# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization-media', '0001_initial'),
        ('organization-projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectAudio',
            fields=[
                ('audio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='organization-media.Audio')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audios', to='organization-projects.Project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'audio',
                'verbose_name_plural': 'audios',
            },
            bases=('organization-media.audio',),
        ),
        migrations.CreateModel(
            name='ProjectVideo',
            fields=[
                ('video_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='organization-media.Video')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='organization-projects.Project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
            },
            bases=('organization-media.video',),
        ),
        migrations.AlterOrderWithRespectTo(
            name='projectvideo',
            order_with_respect_to='project',
        ),
        migrations.AlterOrderWithRespectTo(
            name='projectaudio',
            order_with_respect_to='project',
        ),
    ]