# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameinfo', '0016_auto_20171029_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='gameinfo/desc/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('gameinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameinfo_desc', to='gameinfo.GameInfo')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='gameinfo/faq/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('gameinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameinfo_faq', to='gameinfo.GameInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='gameinfo/setting/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('gameinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameinfo_setting', to='gameinfo.GameInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='gameinfo/summary/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('gameinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameinfo_summary', to='gameinfo.GameInfo')),
            ],
        ),
        migrations.AddField(
            model_name='movies',
            name='cnt',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='movies',
            name='language',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='movies',
            name='subtitle_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='file',
            field=models.FileField(upload_to='gameinfo/movies/file/'),
        ),
        migrations.AlterField(
            model_name='subtitle',
            name='file',
            field=models.FileField(upload_to='gameinfo/movies/subtitle/'),
        ),
    ]