# Generated by Django 5.0.6 on 2024-09-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_playerskins_player_remove_playerskins_prize_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='friend_lvl_2',
            field=models.BooleanField(default=False, verbose_name='Друг выше 2 лвл'),
        ),
        migrations.AddField(
            model_name='player',
            name='tasks',
            field=models.BooleanField(default=False, verbose_name='Выполнены ли задачи'),
        ),
    ]
