# Generated by Django 2.0 on 2018-02-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0009_remove_branch_is_guide'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='forbidden_word_scope',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]