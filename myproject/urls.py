"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import wednesday.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('accounts/', include("accounts.urls")),
    path("app/", include("myapp.urls")),
    path("weather/", include("weather.urls")),
    path("", include("home.urls")),
    path("polls/", include("polls.urls")),
    path("rel/", include("relations.urls")),
    path("newyear/", include("newyear.urls")),
    path("isitwednesday/", wednesday.views.is_wednesday, name="is_wednesday"),
    path('academy/', include('forms.urls')),
    path('nerd/', include('nerd_forms.urls')), # Beispiele für Model Form
    path('exo/', include("exo_planet.urls")),
    path('retro/', include("retro_games.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
