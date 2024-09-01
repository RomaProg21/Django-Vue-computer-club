# Generated by Django 4.2.5 on 2023-11-14 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_usernametelegram'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameTur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameGame', models.CharField(max_length=100, verbose_name='Название игры')),
            ],
            options={
                'verbose_name': 'Игра для турниров',
                'verbose_name_plural': 'Игры для турниров',
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameTournament', models.CharField(max_length=100, verbose_name='Название турнира')),
                ('dateStartTour', models.DateTimeField(verbose_name='Дата Начала турнира')),
                ('comment', models.TextField(max_length=255, verbose_name='Комментарий к турниру')),
                ('gameTour', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.gametur')),
            ],
            options={
                'verbose_name': 'Турнир',
                'verbose_name_plural': 'Турниры',
            },
        ),
        migrations.CreateModel(
            name='PeopleTournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_register', models.DateTimeField(verbose_name='Дата регистрации пользователя на турнир')),
                ('comment', models.CharField(max_length=255, verbose_name='Комментарий')),
                ('TournamentId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.tournament')),
                ('UserIdTour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Бронь на турнир',
                'verbose_name_plural': 'Бронь на турниры',
            },
        ),
    ]