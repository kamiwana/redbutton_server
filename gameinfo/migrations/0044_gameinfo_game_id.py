# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0043_auto_20171127_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameinfo',
            name='game_id',
            field=models.IntegerField(default=0),
        ),
    ]
