# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0039_auto_20171127_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameinfo',
            name='icon',
            field=models.CommaSeparatedIntegerField(blank=True, max_length=100),
        ),
    ]
