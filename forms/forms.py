from django import forms

class SpaceAcademyForm(forms.Form):
    # Name - CharField
    full_name = forms.CharField(
        label="Vollständiger Name",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'William Riker'})
        )
    
    # Email - EmailField
    email = forms.EmailField(
        label="E-Mail",
        widget=forms.EmailInput(attrs={'placeholder': 'riker@enterprise.com'})
    )
    
    # Species - ChoiceField mit Select Dropdown
    species = forms.ChoiceField(
        label="Spezie",
        choices=[
            ('human', 'Mensch'),
            ('vulcan', 'Vulkanier'),
            ('klingon', 'Klingone'),
            ('andorian', 'Andorianer'),
            ('borg', 'Borg (nur Drohnen mit Empfehlung)')
        ],
        widget=forms.Select
    )
    
    # Branch - ChoiceField mit Radio Buttons
    preferred_branch = forms.ChoiceField(
        label="Bevorzugter Zweig",
        choices=[
            ('command', 'Kommando'),
            ('engineering', 'Technik'),
            ('science', 'Wissenschaft'),
            ('medical', 'Medizinisch'),
        ],
        widget=forms.RadioSelect
    )
    
    # Online Profile - URLField
    online_profile = forms.URLField(
        label="Online Profil",
        widget=forms.URLInput(attrs={'placeholder': 'https://enterprise.com'}),
        required=False
    )
    
    # Skills - MultipleChoiceField
    skills = forms.MultipleChoiceField(
        label="Fähigkeiten",
        choices=[
            ('piloting', 'Raumschiff-Pilotierung'),
            ('linguistics', 'Außerirdische Sprachen'),
            ('engineering', 'Warpkern-Engineering'),
            ('diplomacy', 'Diplomatie'),
            ('combat', 'Nahkampf / Taktik')
        ],
        widget=forms.CheckboxSelectMultiple
    )
    
    # Motivation - CharField -> Textarea
    motivation = forms.CharField(
        label="Warum möchtest Du Teil der Akademie werden?",
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Erkläre Deine Motivation'}),
        required=False
    )
    
    # Geburtstag - DateField
    date_of_birth = forms.DateField(
        label="Geburtsdatum",
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
    
    # CV Upload - FileField
    upload_cv = forms.FileField(
        label="Galaktischer Lebenslauf (PDF)",
        required=False
    )
    
    # Terms of Agreement - BooleanField
    agree_to_terms = forms.BooleanField(
        label="Ich stimme den Aufnahmebedingungen zu",
        required=True
    )    
    