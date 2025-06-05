from django.urls import path
from . import views

app_name = "forms"
urlpatterns = [
    path('contact/', views.academy_application, name="academy_contact"),
    path('success/', views.success, name='success'),
]
