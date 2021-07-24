from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import WeatherDetail



urlpatterns = [
    path('', views.index),  
    path('weather/<int:pk>/', WeatherDetail.as_view(), name ='weather'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
