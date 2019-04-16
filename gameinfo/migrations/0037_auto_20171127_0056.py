# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 15:56
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0036_auto_20171127_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameinfo',
            name='icon',
            field=models.CharField(choices=[(1, '어린이추천'), (2, '커플인기'), (3, 'HOT'), (4, '매니아인기'), (5, '남성인기'), (6, '초심자인기'), (7, '직원추천'), (8, '수상작'), (9, '여성인기')], max_length=100, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
