# Generated by Django 4.2.5 on 2023-11-12 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_rename_author_reservation_user1'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsernameTelegram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameTg', models.CharField(max_length=255, verbose_name='Имя телеграм')),
                ('userTg', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Имя телеграмм',
                'verbose_name_plural': 'Имена телеграммов',
            },
        ),
    ]