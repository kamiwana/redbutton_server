# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='auth',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
