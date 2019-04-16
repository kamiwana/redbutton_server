# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0026_auto_20171111_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='gameinfo/')),
                ('div', models.CharField(blank=True, max_length=20)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('gameinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameinfo_gameimage', to='gameinfo.GameInfo')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.RemoveField(
            model_name='image',
            name='gameinfo',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
