# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20160725_0143'),
        ('organization-core', '0005_auto_20160725_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('file', mezzanine.core.fields.FileField(max_length=1024, verbose_name='Image')),
                ('description', models.TextField(blank=True, verbose_name='photo description')),
                ('credits', models.CharField(blank=True, max_length=256, null=True, verbose_name='photo credits')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Page')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name_plural': 'Images',
                'verbose_name': 'Image',
            },
        ),
    ]
