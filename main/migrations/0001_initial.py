# Generated by Django 4.2.6 on 2023-11-05 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('type', models.IntegerField(verbose_name='Тип')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('status', models.IntegerField(verbose_name='Статус')),
                ('vip', models.BooleanField(verbose_name='Вип')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудования',
            },
        ),
        migrations.CreateModel(
            name='Periphery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(verbose_name='Тип')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Периферия',
                'verbose_name_plural': 'Периферии',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(verbose_name='Начало')),
                ('end_date', models.DateTimeField(verbose_name='Конец')),
                ('comment', models.TextField(max_length=255, verbose_name='Комментарий')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.equipment')),
                ('periphery', models.ManyToManyField(blank=True, to='main.periphery')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирования',
            },
        ),
    ]