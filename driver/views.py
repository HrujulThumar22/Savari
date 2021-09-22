from driver.forms import TripCreationForm
from django.shortcuts import render

# Create your views here.
def StartJourney(request):
    form=TripCreationForm()
    context={'form':form}
    return render(request,'driver/startJourney.html',context)
