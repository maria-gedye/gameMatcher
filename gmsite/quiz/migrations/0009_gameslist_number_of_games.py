# Generated by Django 4.0.4 on 2022-06-21 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_game_gameslist'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameslist',
            name='number_of_games',
            field=models.IntegerField(default=0),
        ),
    ]
