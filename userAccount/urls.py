from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="user_home"),
    path('signup/',views.driverSignup,name="register_user"),
    path('update/<str:pk>/',views.updateUser,name="update_user"),
]
