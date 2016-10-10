# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-23 10:19
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.pages.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20160804_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='in_menus',
            field=mezzanine.pages.fields.MenusField(blank=True, choices=[(1, 'Action'), (2, 'Departement'), (3, 'Footer vertical'), (4, 'Footer horizontal'), (5, 'Magazine'), (6, 'Vous êtes')], max_length=100, null=True, verbose_name='Show in menus'),
        ),
    ]