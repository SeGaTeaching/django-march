import requests
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def weather_view(request):
    API_KEY = "e840120397fd69790c9ff22e5f354b0f"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_KEY
    
    if request.method == 'POST':
        city_name = request.POST.get('city')
    
        response = requests.get(url.format(city_name))
        if response.status_code == 200:
            data = response.json()
            weather = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            return render(request, 'weather/weather.html', {'weather': weather})
        else:
             return render(request, 'weather/weather.html', {'error': 'Stupid, that is nor a real place!'})
    else:
        return render(request, 'weather/weather.html')

# def weather_widget(request):
#     city = request.GET.get('city', 'London')
#     API_KEY = config('WEATHER_API_KEY')
    
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + API_KEY
#     response = requests.get(url.format(city))
    
#     if response.status_code == 200:
#         data = response.json()
#         weather = {
#             'city': data['name'],
#             'temperature': data['main']['temp'],
#             'description': data['weather'][0]['description'],
#             'icon': data['weather'][0]['icon']
#         }
#         return JsonResponse(weather)
#     else:
#         return JsonResponse({'error': 'City not found'}, status=404)