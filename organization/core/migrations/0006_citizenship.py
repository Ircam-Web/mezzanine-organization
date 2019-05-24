# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-05-16 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-core', '0005_linktype_fa_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizenship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]