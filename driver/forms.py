from django.forms import ModelForm,widgets
from django.forms import fields, models
from .models import DriverTrip

class TripCreationForm(ModelForm):
    class Meta:
        model=DriverTrip
        fields=['Starting_City','Destination_City','Trip_Starting_Date','Trip_Starting_Time','Trip_Ending_Date','Trip_Ending_Time']
        widgets={'Trip_Starting_Date':widgets.DateInput(attrs={'type':'date'}),'Trip_Ending_Date':widgets.DateInput(attrs={'type':'date'}),'Trip_Starting_Time':widgets.TimeInput(attrs={'type':'time'}),'Trip_Ending_Time':widgets.TimeInput(attrs={'type':'time'})}