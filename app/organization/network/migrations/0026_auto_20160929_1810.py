# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-09-29 16:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0025_auto_20160928_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityframework',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='activityframework',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='activityframework',
            name='name_en',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='activityframework',
            name='name_fr',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='activityfunction',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='activityfunction',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='activityfunction',
            name='name_en',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='activityfunction',
            name='name_fr',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='activitygrade',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='activitygrade',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='activitygrade',
            name='name_en',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='activitygrade',
            name='name_fr',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='activitystatus',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='activitystatus',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='activitystatus',
            name='name_en',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='activitystatus',
            name='name_fr',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='traininglevel',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='traininglevel',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='traininglevel',
            name='name_en',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='traininglevel',
            name='name_fr',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='trainingspeciality',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='trainingspeciality',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='trainingspeciality',
            name='name_en',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='trainingspeciality',
            name='name_fr',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='trainingtopic',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='trainingtopic',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='trainingtopic',
            name='name_en',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='trainingtopic',
            name='name_fr',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='trainingtype',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='trainingtype',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='trainingtype',
            name='name_en',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='trainingtype',
            name='name_fr',
            field=models.CharField(max_length=512, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='personactivity',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='organization-network.Person', verbose_name='person'),
        ),
    ]
