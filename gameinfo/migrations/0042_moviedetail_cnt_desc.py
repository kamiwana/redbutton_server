# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 03:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0041_auto_20171127_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedetail',
            name='cnt_desc',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
