from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exoplanet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    radius_km = models.FloatField()
    orbit_type = models.CharField(max_length=50, choices=[
        ('circular', 'Kreisförmig'),
        ('elliptical', 'Elliptisch'),
        ('hyperbolic', 'Hyperbolisch')
    ])
    habitable = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
