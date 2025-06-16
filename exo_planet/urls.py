from django.urls import path
from . import views

app_name = 'exo_planet'
urlpatterns = [
    path('planet-list/', views.planet_list, name='planet_list'),
    path('add-planet/', views.add_planet, name='add_planet'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('planet/<int:planet_id>/edit/', views.edit_planet, name='edit_planet'),
    path('planet/<int:planet_id>/delete/', views.delete_planet, name='delete_planet'),
]
