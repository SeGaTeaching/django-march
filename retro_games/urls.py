from django.urls import path
from . import views

app_name="retro_games"
urlpatterns = [
    path('', views.game_list, name="game_list"),
    path('upload', views.upload_game, name="upload_game"),
]
