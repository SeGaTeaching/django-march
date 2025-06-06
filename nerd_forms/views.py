from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VillainGearForm, WandLicenseForm
from .models import VillainGear, WandLicense

# Create your views here.
def register_gear(r):
    
    if r.method == 'POST':
        # form Objekt mit Daten aus Formular füllen
        form = VillainGearForm(r.POST)
        
        # Überprüfung ob FormularDaten korrekt sind
        if form.is_valid():
            
            # Daten in der Datenbank speichern
            obj = form.save()
            
            return redirect('nerd_forms:gear_success', pk=obj.id)
            
            
            # return HttpResponse(f"""
            #                     <h2>Deine Daten wurden erfolgreich gespeichert</h2>
            #                     <p>Owner: {obj.owner_alias}</p>
            #                     <p>Gear Name: {obj.gear_name}</p>
            #                     <p>Gear Type: {obj.gear_type}</p>
            #                     <p>Power: {obj.power_rating}</p>
            #                     """)

    form = VillainGearForm()
    return render(r, 'nerd_forms/gear_form.html', {'formular': form})

def gear_success(r, pk):
    gear = VillainGear.objects.get(pk=pk)
    
    return render(r, 'nerd_forms/gear_success.html', {'gear': gear})


#------------------------------------------------------
# Wand License Example for more individual Form Fields
#------------------------------------------------------
def wand_license(request):
    
    if request.method == 'POST':
        form = WandLicenseForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            if not form.cleaned_data['confirm_magic_code']:
                form.add_error('confirm_magic_code', 'Du kannst nur Deine Daten übermitteln, wenn Du unseren Code akzpetierst')
            else:
                obj.save()
                return redirect('nerd_forms:wand_success', pk=obj.id)
    
    form = WandLicenseForm()
    return render(request, 'nerd_forms/wand_form.html', {"form": form})

def wand_success(request, pk):
    return render(request, 'nerd_forms/wand_success.html') 