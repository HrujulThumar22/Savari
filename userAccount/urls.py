from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="user_home"),
    path('login/',views.handleLogin,name="user_login"),
    path('signup/',views.signup,name="register_user"),
    path('update/<str:pk>/',views.updateUser,name="update_user"),
    path('logout',views.handleLogout,name="user_logout")
]
