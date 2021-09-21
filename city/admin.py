from django.contrib import admin

# Register your models here.
from .models import Country,State,City

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
