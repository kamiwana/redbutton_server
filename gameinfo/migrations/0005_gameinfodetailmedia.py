# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0004_auto_20171019_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameInfoDetailMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameinfo_idx', models.IntegerField()),
                ('movie_title', models.CharField(blank=True, max_length=255)),
                ('movie_file', models.FileField(upload_to='movie/file/')),
                ('movie_uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('smi_title', models.CharField(blank=True, max_length=255)),
                ('smi_file', models.FileField(upload_to='movie/smi/')),
                ('cnt', models.CharField(blank=True, max_length=10)),
                ('language', models.CharField(blank=True, max_length=10)),
                ('smi_uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
