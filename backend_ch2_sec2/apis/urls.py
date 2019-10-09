from django.contrib import admin
from django.urls import path
from .views import weather

urlpatterns = [
    path('weather', weather.weather)
]