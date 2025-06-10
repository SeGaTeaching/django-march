from django import forms
from .models import Exoplanet

class ExoplanetForm(forms.ModelForm):
    class Meta:
        model = Exoplanet
        fields = '__all__'
        
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            #'orbit_type': forms.RadioSelect
        }
        
        
class CSVUploadForm(forms.Form):
    file = forms.FileField(label='Upload CSV-File')