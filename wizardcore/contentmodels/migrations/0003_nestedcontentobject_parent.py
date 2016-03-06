# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-05 23:14
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contentmodels', '0002_nestedcontentobject'),
    ]

    operations = [
        migrations.AddField(
            model_name='nestedcontentobject',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='contentmodels.NestedContentObject'),
        ),
    ]