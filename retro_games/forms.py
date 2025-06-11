from django import forms
from .models import RetroGame

class RetroGameForm(forms.ModelForm):
    class Meta:
        model = RetroGame
        fields = '__all__'