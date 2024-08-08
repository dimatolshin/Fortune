# Generated by Django 5.0.6 on 2024-08-07 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_player_now_energy_upgrade_coin_bonus_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='upgrade',
            name='start_autobot_time',
            field=models.PositiveBigIntegerField(default=300),
        ),
        migrations.AlterField(
            model_name='upgrade',
            name='coin_bonus_result',
            field=models.IntegerField(default=0),
        ),
    ]