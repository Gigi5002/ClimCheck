from django.conf import settings
from django.shortcuts import render, redirect
import requests

OPEN_METEO_API_URL = "https://api.open-meteo.com/v1/forecast"
OPENCAGE_API_URL = "https://api.opencagedata.com/geocode/v1/json"


def get_coordinates(city):
    if not settings.OPEN_CAGE_API_KEY:
        raise ValueError("API key for OpenCage is not set in environment variables.")

    response = requests.get(OPENCAGE_API_URL, params={
        'q': city,
        'key': settings.OPEN_CAGE_API_KEY
    })
    data = response.json()
    if data['results']:
        location = data['results'][0]['geometry']
        return location['lat'], location['lng']
    return None, None


def get_weather(city):
    latitude, longitude = get_coordinates(city)
    if latitude is None or longitude is None:
        return {'city': city, 'temperature': None, 'condition': 'Not Found'}

    response = requests.get(OPEN_METEO_API_URL, params={
        'latitude': latitude,
        'longitude': longitude,
        'hourly': 'temperature_2m',
        'timezone': 'Asia/Bishkek'
    })
    data = response.json()
    temperature = data.get('hourly', {}).get('temperature_2m', [])[0] if 'hourly' in data else None

    return {
        'city': city,
        'temperature': temperature,
        'condition': 'Clear'  # Замените на реальное состояние, если доступно
    }


def weather_view(request):
    city = request.GET.get('city', '')
    weather = None
    history = request.session.get('search_history', [])

    if city:
        try:
            weather = get_weather(city)
            if city not in history:
                history.append(city)
                request.session['search_history'] = history
        except ValueError as e:
            return render(request, 'weather_app/weather.html', {'error': str(e), 'history': history})

    return render(request, 'weather_app/weather.html', {'weather': weather, 'history': history})


def home_view(request):
    return redirect('/weather/')
