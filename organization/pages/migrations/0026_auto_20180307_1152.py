# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-03-07 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization-pages', '0025_auto_20171222_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_css', models.CharField(max_length=32)),
                ('link', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='link_style', to='pages.Link', verbose_name='link')),
            ],
            options={
                'verbose_name': 'css class',
            },
        ),
        migrations.AlterField(
            model_name='home',
            name='slug',
            field=models.CharField(blank=True, default='', help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, verbose_name='URL'),
            preserve_default=False,
        ),
    ]