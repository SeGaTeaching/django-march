from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SpaceAcademyForm
from .models import AcademyApplication

# Create your views here.
def academy_application(request):
    
    # Post Request Code
    if request.method == 'POST':
        
        # 1. Neues Form-Objekt erstellen und mit gesendeten Formular-Daten füllen
        form_filled = SpaceAcademyForm(request.POST, request.FILES)
        
        # 2. Validierung der Daten und auslesen
        if form_filled.is_valid():
            
            name = form_filled.cleaned_data['full_name']
            email = form_filled.cleaned_data['email']
            species = form_filled.cleaned_data['species']
            branch = form_filled.cleaned_data['preferred_branch']
            profile = form_filled.cleaned_data['online_profile']
            skills = form_filled.cleaned_data['skills']
            motiv = form_filled.cleaned_data['motivation']
            birthdate = form_filled.cleaned_data['date_of_birth']
            cv = form_filled.cleaned_data['upload_cv']
            terms = form_filled.cleaned_data['agree_to_terms']
            
        # 3 Daten verarbeiten (DB Speichern)
        content = f"""
        <p>Vielen Dank für Deine Daten</p>
        <ul>
        <li>Name: {name}</li>
        <li>E-Mail: {email}</li>
        <li>Spezie: {species}</li>
        <li>Bereich: {branch}</li>
        <li>Profil: {profile}</li>
        <li>Fähigkeiten: {skills}</li>
        <li>Motiv: {motiv}</li>
        <li>Geburtstag: {birthdate}</li>
        <li>Lebenslauf: {cv}</li>
        <li>Bedingungen: {terms}</li>
        </ul>
        """
        
        # 4. Antwort zurück an den Client (Beispiel)
        #return HttpResponse(content)
        
        # 5 Die aller aller Beste Methode - Daten in DB speichern
        AcademyApplication.objects.create(**form_filled.cleaned_data)
        
        # 6. Showcase - Daten in Session-ID-Cookie speichern
        form_filled.cleaned_data['date_of_birth'] = form_filled.cleaned_data['date_of_birth'].strftime("%d.%m.%Y")
        request.session["form-data"] = form_filled.cleaned_data
    
        # 7 Bestätigungsseite aufrufen
        return redirect('forms:success')
        
    # Get Request Code
    form = SpaceAcademyForm()
    return render(request, 'forms/application.html', {'form': form})

def success(request):
    data = request.session['form-data']
    
    return render(request, 'forms/success.html', {'data': data})