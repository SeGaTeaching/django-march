from django.urls import path
from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.weather_view, name='weather'),
    #path('api/', views.weather_widget, name='weather_widget')
]
