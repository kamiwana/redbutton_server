# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-06 04:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0008_branch_is_guide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='is_guide',
        ),
    ]
