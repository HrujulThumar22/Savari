from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('start/',views.StartJourney,name="driver_start"),
]