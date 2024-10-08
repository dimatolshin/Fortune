# Generated by Django 5.0.6 on 2024-09-11 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_leagueskins_player_remove_playerskins_player_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leagueskins',
            name='player',
            field=models.ManyToManyField(blank=True, related_name='league_skins', to='main.player', verbose_name='Игрок'),
        ),
        migrations.AlterField(
            model_name='playerskins',
            name='player',
            field=models.ManyToManyField(blank=True, related_name='player_skins', to='main.player', verbose_name='Игрок'),
        ),
    ]
