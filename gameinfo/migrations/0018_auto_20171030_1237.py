# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0017_auto_20171029_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='cnt',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
