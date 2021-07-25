from django.urls import path
from . import views
from .views import WeatherDetail

urlpatterns = [
    path('weather/', WeatherDetail.as_view(), name ='weather'),
]
