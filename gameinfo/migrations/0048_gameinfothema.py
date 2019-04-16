# Generated by Django 2.0 on 2018-04-12 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_thema', '0001_initial'),
        ('gameinfo', '0047_auto_20180406_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameInfoThema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gameinfo_thema', to='gameinfo.GameInfo')),
                ('thema', models.ManyToManyField(related_name='game_thema', to='game_thema.GameThema')),
            ],
        ),
    ]