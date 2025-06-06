from django.urls import path
from . import views

app_name = "nerd_forms"
urlpatterns = [
    path('villain/', views.register_gear, name="register_gear"),
    path('villain/success/<int:pk>/', views.gear_success, name='gear_success'),
    path('magic/', views.wand_license, name='wand_license'),
    path('magic/success/<int:pk>/', views.wand_success, name='wand_success'),
    
]
