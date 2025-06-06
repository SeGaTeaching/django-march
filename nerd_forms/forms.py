from django import forms
from .models import VillainGear, WandLicense

class VillainGearForm(forms.ModelForm):
    class Meta:
        model = VillainGear
        fields = '__all__'


       
#------------------------------------------------------
# Wand License Example for more individual Form Fields
#------------------------------------------------------
        
class WandLicenseForm(forms.ModelForm):
    confirm_magic_code = forms.BooleanField(
        label="Ich bezeuge, dass ich keine verbotene Magie praktiziere",
        required=False
    )
    
    class Meta:
        model = WandLicense
        fields = [
            'full_name', 'birth_date', 'wand_length_cm',
            'wand_core', 'has_dark_mark', 'patronus_description',
            'magical_law_acknowledged'
        ]
        
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'wand_length_cm': forms.NumberInput(attrs={'step': '0.5', 'min': '10', 'max': '50'}),
            'patronus_description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Optional, z.B. "Otter"'}),
        }
        
        labels = {
            'full_name': 'Name',
            'birth_date': 'Geburtsdatum',
            'wand_length_cm': 'Zauberstablänge (in cm)',
            'wand_core': 'Kernmaterial',
            'has_dark_mark': 'Trägst du das Dunkle Mal?',
            'patronus_description': 'Beschreibe deinen Patronus (optional)',
            'magical_law_acknowledged': 'Ich kenne das Internationale Zauberei-Gesetz'
        }
        
        help_texts = {
            'wand_core': 'Der Kern deines aktuellen Zauberstabs',
            'wand_length_cm': 'Bitte auf Zehntel genau angeben (z. B. 32.5)',
        }
        
        error_messages = {
            'full_name': {
                'required': 'Dein Name wird zur Lizenzprüfung benötigt.',
            },
            'birth_date': {
                'invalid': 'Bitte gib ein gültiges Geburtsdatum an.',
            }
        }