from django.shortcuts import render, redirect
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
    games = RetroGame.objects.all().order_by('-year')
    return render(request, 'retrogames/list.html', {'games': games})