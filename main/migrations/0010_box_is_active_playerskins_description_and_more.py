# Generated by Django 5.0.6 on 2024-09-03 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_playerskins'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='playerskins',
            name='description',
            field=models.CharField(default='', max_length=100, verbose_name='Описание скина'),
        ),
        migrations.AddField(
            model_name='playerskins',
            name='name',
            field=models.CharField(default='', max_length=30, verbose_name='Название скина'),
        ),
        migrations.CreateModel(
            name='TaskPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='Название задачи')),
                ('description', models.CharField(default='', max_length=100, verbose_name='Описание задачи')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка на аккаунт для выполнения задания')),
                ('completed', models.BooleanField(default=False, verbose_name='Выполнено/не выполнено')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна/неактивна')),
                ('player', models.ManyToManyField(related_name='players_task', to='main.player', verbose_name='Игрок')),
            ],
        ),
    ]
