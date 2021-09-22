from django import forms
from django.forms import fields, models
from .models import DriverTrip

class TripCreationForm(forms.ModelForm):
    class Meta:
        model=DriverTrip
        fields=['Starting_City','Destination_City','Trip_Starting_Time','Trip_Ending_Time']