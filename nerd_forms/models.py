from django.db import models
from django.utils import timezone


# Create your models here.
choices = [
    ('weapon', 'Waffe'),
    ('vehicle', 'Fahrzeug'),
    ('robot', 'Roboter'),
    ('tool', 'Werkzeug'),
    ('ai', 'Künstliche Intelligenz')
]

class VillainGear(models.Model):
    owner_alias = models.CharField(max_length=100)
    gear_name = models.CharField(max_length=100)
    gear_type = models.CharField(max_length=20, choices=choices)
    origin_year = models.PositiveIntegerField()
    explosive = models.BooleanField(default=False)
    #last_maintenance = models.DateField()
    power_rating = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.gear_name} ({self.owner_alias})"
    
CORES = [
    ('phoenix', 'Phönixfeder'),
    ('dragon', 'Drachenherzfaser'),
    ('unicorn', 'Einhornhaar'),
    ('thestral', 'Thestralschweif')
]

class WandLicense(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    wand_length_cm = models.DecimalField(max_digits=4, decimal_places=1)
    wand_core = models.CharField(max_length=20, choices=CORES)
    has_dark_mark = models.BooleanField(default=False)
    patronus_description = models.TextField(blank=True)
    license_requested_on = models.DateTimeField(default=timezone.now)
    magical_law_acknowledged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} – Lizenzantrag"
    
    class Meta:
        ordering = ['-license_requested_on']