# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 20:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentmodels', '0006_auto_20160306_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nestedcontentobject',
            name='parent',
        ),
        migrations.DeleteModel(
            name='NestedContentObject',
        ),
    ]