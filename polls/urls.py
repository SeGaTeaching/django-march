from django.urls import path
from . import views

urlpatterns = [
    path("", views.polls, name="polls"),
    path("<int:pk>", views.example_detail_view, name="detail_view")
]