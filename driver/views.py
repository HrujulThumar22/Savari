from driver.forms import TripCreationForm
from django.shortcuts import redirect, render

# Create your views here.
def StartJourney(request):
    if request.method=="POST":
        form=TripCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_home')
        else:
            return redirect('driver_start')
    form=TripCreationForm()
    context={'form':form}
    return render(request,'driver/startJourney.html',context)
