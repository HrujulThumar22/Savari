"""savari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from . import views
import notifications.urls
from django.conf import settings 
from django.urls import include
from django.conf.urls.static import static

admin.site.site_header  =  "Savari System admin"  
admin.site.site_title  =  "Savari System site"
admin.site.index_title  =  "Savari System Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('userAccount.urls')),
    path('driver/',include('driver.urls')),
    path('rides/',include('passengerTrip.urls')),
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
