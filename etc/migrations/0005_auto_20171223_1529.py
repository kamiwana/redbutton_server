# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etc', '0004_auto_20171223_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customopinion',
            name='uploaded_at',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='etc',
            name='uploaded_at',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]