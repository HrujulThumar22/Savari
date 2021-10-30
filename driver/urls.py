from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings 
from django.urls import include
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Home,name="driver_home"),
    path('start/',views.StartJourney,name="driver_start"),
    path('request/',views.RideRequest,name="driver_request"),
    path('ridedetail/<str:pk>/',views.RideDetail.as_view(),name="driver_ride"),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)