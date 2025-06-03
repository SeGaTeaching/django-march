from django.urls import path
from . import views

urlpatterns = [
    path('', views.relations, name="relations")
]
