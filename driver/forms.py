from django.forms import ModelForm,widgets
from .models import DriverTrip
from city.models import City

class TripCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TripCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=DriverTrip
        fields=['Starting_City','Destination_City','Vehicle_Name','Vehicle_Number','Vacancy','Stops','vehicleimg']