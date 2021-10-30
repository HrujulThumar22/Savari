from typing import ChainMap
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings 
from django.urls import include
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="user_home"),
    path('login/',views.handleLogin,name="user_login"),
    path('signup/',views.signup,name="register_user"),
    path('update/<str:pk>/',views.updateUser,name="update_user"),
    path('logout',views.handleLogout,name="user_logout"),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('detail/<str:pk>/',views.UserDetail.as_view(), name='user_detail'),
    path('changepass/<str:pk>/',views.changepass, name='change_pass'),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)