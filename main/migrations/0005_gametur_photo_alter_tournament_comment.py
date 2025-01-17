# Generated by Django 4.2.6 on 2023-11-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_gametur_tournament_peopletournament'),
    ]

    operations = [
        migrations.AddField(
            model_name='gametur',
            name='photo',
            field=models.ImageField(height_field=100, null=True, upload_to='images/', width_field=100),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='comment',
            field=models.TextField(max_length=999, verbose_name='Комментарий к турниру'),
        ),
    ]
