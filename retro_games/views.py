from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RetroGameForm
from .models import RetroGame

# Create your views here.

def upload_game(request):
    if request.method == 'POST':
        form = RetroGameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('retro_games:game_list')
    else:
        form = RetroGameForm()
        
    return render(request, 'retrogames/upload.html', {'form': form})

def game_list(request):
    try:
        games = RetroGame.objects.all().order_by('-year')
    except:
        return HttpResponse(f'<h2>Es konnten keine Daten auf dem Server gefunden werden, bzw. die Datenbank ist momentan nicht erreichbar</h2>')
    return render(request, 'retrogames/list.html', {'games': games})