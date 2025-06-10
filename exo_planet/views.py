import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ExoplanetForm, CSVUploadForm
from .models import Exoplanet

# Create your views here.
@login_required(login_url='accounts:login')
def add_planet(request):
    if request.method == 'POST':
        form = ExoplanetForm(request.POST)
        if form.is_valid():
            planet = form.save(commit=False)
            planet.user = request.user
            planet.save()
            return redirect('exo_planet:planet_list')
    
    # if method ist 'GET'
    form = ExoplanetForm()
    return render(request, 'exo_planet/add_planet.html', {'form': form})

@login_required(login_url='accounts:login')
def planet_list(request):
    planets = Exoplanet.objects.filter(user=request.user)
    return render(request, 'exo_planet/planet_list.html', {'planets': planets})

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES.get('file')
            # Check if file is a csv file
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Please upload only CSV files.')
                return render(request, 'movies/upload_csv.html', {'form': form})
            
            # Dekodieren und Zeilen einlesen
            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(decoded_file)
                print(f'this is what I see: {reader}')

                for row in reader:
                    Exoplanet.objects.create(
                        user=request.user,
                        name=row['name'],
                        radius_km=row['radius_km'],
                        orbit_type=row['orbit_type'],
                        habitable=row['habitable'],
                        description=row['description']
                    )
                return redirect('exo_planet:planet_list')
            
            except Exception as e:
                messages.error(request, f'Error while handling file: {str(e)}')
    else:
        form = CSVUploadForm()
    return render(request, 'exo_planet/upload_csv.html', {'form': form})
