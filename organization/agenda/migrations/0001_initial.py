# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mezzanine_agenda', '0003_remove_event_blog_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('title', models.CharField(max_length=1024, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('with_separator', models.BooleanField(default=False)),
                ('background_color', models.CharField(blank=True, choices=[('black', 'black'), ('yellow', 'yellow'), ('red', 'red')], max_length=32, verbose_name='background color')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blocks', to='mezzanine_agenda.Event', verbose_name='event')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name_plural': 'blocks',
                'verbose_name': 'block',
            },
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('title', models.CharField(max_length=1024, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('file', mezzanine.core.fields.FileField(max_length=1024, verbose_name='Image')),
                ('credits', models.CharField(blank=True, max_length=256, null=True, verbose_name='credits')),
                ('type', models.CharField(choices=[('logo', 'logo'), ('slider', 'slider'), ('card', 'card'), ('page_slider', 'page slider')], max_length=64, verbose_name='type')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='mezzanine_agenda.Event', verbose_name='event')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name_plural': 'images',
                'verbose_name': 'image',
            },
        ),
    ]