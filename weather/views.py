from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import Weather
from .serializers import WeatherSerializer
import requests
 
class WeatherDetail(ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def list(self, request):
        city = 'canberra'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=c99159f47dfcfa9dce5fbc667a06d2e2'
        city_weather = requests.get(url).json() 
        print(city_weather)
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
        }    
        return JsonResponse(weather)
