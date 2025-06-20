# Generated by Django 5.2.1 on 2025-06-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retro_games', '0003_alter_retrogame_console'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retrogame',
            name='console',
            field=models.CharField(choices=[('nes', 'NES'), ('snes', 'SNES'), ('n64', 'Nintendo 64'), ('ps1', 'PlayStation 1'), ('pc', 'Windows PC')], max_length=100),
        ),
    ]
