from django.contrib import admin
from .models import DriverTrip
# Register your models here.
class DriverTripAdmin(admin.ModelAdmin):
    readonly_fields  = ('Trip_Created_On',)

admin.site.register(DriverTrip,DriverTripAdmin)