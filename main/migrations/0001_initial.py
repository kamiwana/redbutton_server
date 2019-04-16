# Generated by Django 2.2 on 2019-04-05 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='main/layer/')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('type', models.CharField(choices=[(1, 'Type01')], max_length=10)),
                ('div', models.SmallIntegerField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(blank=True, max_length=150)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='layer', to='branch.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='LayerSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='main/layer/sub')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(blank=True, max_length=150)),
                ('layer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='layer_sub', to='main.Layer')),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='main/guide/')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(blank=True, max_length=150)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guide', to='branch.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='main/course/')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(blank=True, max_length=150)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='branch.Branch')),
            ],
        ),
    ]
