# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 19:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentmodels', '0005_nestedcontentobject_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentobject',
            name='content',
        ),
        migrations.RemoveField(
            model_name='nestedcontentobject',
            name='content',
        ),
    ]