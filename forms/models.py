from django.db import models

# Create your models here.
# space/models.py
from django.db import models

class AcademyApplication(models.Model):
    BRANCH_CHOICES = [
        ('command', 'Kommando'),
        ('engineering', 'Technik'),
        ('science', 'Wissenschaft'),
        ('medical', 'Medizinisch'),
    ]

    SPECIES_CHOICES = [
        ('human', 'Mensch'),
        ('vulcan', 'Vulkanier'),
        ('klingon', 'Klingone'),
        ('andorian', 'Andorianer'),
        ('borg', 'Borg (nur Drohnen mit Empfehlung)'),
    ]

    SKILL_CHOICES = [
        ('piloting', 'Raumschiff-Pilotierung'),
        ('linguistics', 'Außerirdische Sprachen'),
        ('engineering', 'Warpkern-Engineering'),
        ('diplomacy', 'Diplomatie'),
        ('combat', 'Nahkampf / Taktik'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    preferred_branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    online_profile = models.URLField(blank=True)
    skills = models.JSONField()  # list of strings
    motivation = models.TextField(blank=True)
    date_of_birth = models.DateField()
    upload_cv = models.FileField(upload_to='uploads/cvs/', blank=True, null=True)
    agree_to_terms = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.email})"
