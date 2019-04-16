# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('created_date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('idx', models.IntegerField()),
                ('game_name', models.CharField(max_length=50)),
                ('genre', models.CharField(blank=True, max_length=50)),
                ('media', models.IntegerField()),
                ('setting', models.IntegerField()),
                ('desc', models.IntegerField()),
            ],
        ),
    ]