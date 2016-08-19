# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-09 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization-project', '0003_auto_20160808_0118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectblock',
            options={},
        ),
        migrations.AlterModelOptions(
            name='projectimage',
            options={'ordering': ('_order',)},
        ),
        migrations.AlterModelOptions(
            name='projectlink',
            options={'verbose_name': 'link', 'verbose_name_plural': 'links'},
        ),
        migrations.AddField(
            model_name='projectblock',
            name='content_en',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='projectblock',
            name='content_fr',
            field=mezzanine.core.fields.RichTextField(null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='projectblock',
            name='title_en',
            field=models.CharField(max_length=1024, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='projectblock',
            name='title_fr',
            field=models.CharField(max_length=1024, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='description_fr',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='projectblock',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blocks', to='organization-project.Project', verbose_name='project'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='credits',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='credits'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='organization-project.Project'),
        ),
        migrations.AlterField(
            model_name='projectlink',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='organization-project.Project'),
        ),
    ]