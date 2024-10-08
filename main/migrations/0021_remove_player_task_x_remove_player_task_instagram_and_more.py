# Generated by Django 5.0.6 on 2024-09-19 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_remove_taskplayer_completed_remove_taskplayer_player_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='task_X',
        ),
        migrations.RemoveField(
            model_name='player',
            name='task_instagram',
        ),
        migrations.RemoveField(
            model_name='player',
            name='task_tg_channel',
        ),
        migrations.RemoveField(
            model_name='player',
            name='task_tg_group',
        ),
        migrations.RemoveField(
            model_name='playertask',
            name='player',
        ),
        migrations.RemoveField(
            model_name='playertask',
            name='task',
        ),
        migrations.AddField(
            model_name='playertask',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_player', to='main.player', verbose_name='Игрок'),
        ),
        migrations.AddField(
            model_name='playertask',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_tasks', to='main.taskplayer', verbose_name='Задача'),
        ),
    ]
