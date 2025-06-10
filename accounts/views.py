from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserRegistrationForm
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account für {username} wurde erstellt. Juhu!')
            return redirect("accounts:login")
    else:
        form = CustomUserRegistrationForm()
            
    return render(request, 'accounts/register.html', {'form': form})
    
def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Methode 1 um den user zu bekommen
            # Beste Methode für Standard Login Formular
            user = form.get_user()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, f'{username} ist jetzt eingeloggt')
            return redirect('exo_planet:planet_list')
            
            # Methode 2 um den user aus der Datenbank zu fischen
            # gut für eigene Logik bei individuellen Login Formularen 
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            
            # user = authenticate(username=username, password=password) # Überprüfung ob Anmeldedaten übereinstimmen
            # if user is not None:
            #     login(request, user)
            #     messages.success(request, f'{username} ist jetzt eingeloggt')
            #     return redirect('exo_planet:planet-list')
    else: 
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def user_profile(request):
    return render(request, 'accounts/profile.html')
    