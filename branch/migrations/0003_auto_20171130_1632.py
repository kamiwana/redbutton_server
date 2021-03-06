# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_auto_20171121_0007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'ordering': ['-branch_code']},
        ),
        migrations.AddField(
            model_name='branch',
            name='branch_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='branch_user',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='forbidden_word_cnt',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='game_cnt',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
