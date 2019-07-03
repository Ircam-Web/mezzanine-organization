# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-03-26 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('organization-network', '0129_merge_20190221_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicContentPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('object_id', models.PositiveIntegerField(editable=False, null=True, verbose_name='related object')),
                ('content_type', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='content type')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dynamic_content_person', to='organization-network.Person', verbose_name='person')),
            ],
            options={
                'verbose_name': 'Dynamic Content Person',
                'ordering': ('_order',),
            },
        ),
    ]