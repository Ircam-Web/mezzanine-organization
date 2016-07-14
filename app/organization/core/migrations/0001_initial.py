# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('sub_title', models.TextField(blank=True, max_length=1024, verbose_name='sub title')),
                ('sub_title_fr', models.TextField(blank=True, max_length=1024, null=True, verbose_name='sub title')),
                ('sub_title_en', models.TextField(blank=True, max_length=1024, null=True, verbose_name='sub title')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'basic page',
            },
            bases=('pages.page', models.Model),
        ),
    ]
