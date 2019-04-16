# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0021_auto_20171108_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviedetail',
            name='movie_id',
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='movie_id',
            field=models.IntegerField(null=True),
        ),
        migrations.RemoveField(
            model_name='moviedetail',
            name='subtitle_id',
        ),
        migrations.AddField(
            model_name='moviedetail',
            name='subtitle_id',
            field=models.IntegerField(null=True),
        ),
    ]
