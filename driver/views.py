from decorators.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from driver.forms import TripCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from userAccount.models import User
from .models import DriverTrip
# Create your views here.
@login_required
@allowed_users(allowed_role=['driver'])
def StartJourney(request):
    if request.method=="POST":
        form=TripCreationForm(request.POST)
        user=get_object_or_404(User,pk=request.user.id)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.Driver=user
            trip.save()
            return redirect('driver_home')
        else:
            return redirect('driver_start')
    form=TripCreationForm()
    context={'form':form}
    return render(request,'driver/startJourney.html',context)
@login_required
@allowed_users(allowed_role=['driver'])
def Home(request):
    trips=DriverTrip.objects.filter(Driver_id=request.user.id)
    if trips.exists():
        context={'trips':trips}
    else:
        context={'trips':False}
    return render(request,'driver/home.html',context)

