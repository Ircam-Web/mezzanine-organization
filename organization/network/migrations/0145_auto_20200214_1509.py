# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-02-14 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0144_auto_20200116_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('neutral', 'neutral'), ('prefer not to disclose', 'prefer not to disclose')], max_length=16, verbose_name='gender'),
        ),
    ]