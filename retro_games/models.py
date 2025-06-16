from django.db import models

# Create your models here.
class RetroGame(models.Model):
    CONSOLES = [
        ('gameboy', 'Gameboy'),
        ('nes', 'NES'),
        ('snes', 'SNES'),
        ('n64', 'Nintendo 64'),
        ('ps1', 'PlayStation 1'),
        ('pc', 'Windows PC'),
    ]

    title = models.CharField(max_length=100)
    console = models.CharField(max_length=100, choices=CONSOLES)
    year = models.PositiveIntegerField()
    game_cover = models.ImageField(upload_to='retrogames/covers/')

    def __str__(self):
        return f"{self.title} ({self.get_console_display()})"