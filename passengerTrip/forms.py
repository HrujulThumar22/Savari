from django.forms import ModelForm,widgets
from .models import UserTrip,BookRide
from city.models import City

class BookRideForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookRideForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=BookRide
        fields=['Starting_City','Destination_City']

class ConfirmRideForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConfirmRideForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model=UserTrip
        labels={'noOfSeatsBooked':('Enter number of Seats Required')}
        fields=['noOfSeatsBooked']