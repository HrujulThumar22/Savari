from django.contrib.auth.decorators import login_required
from driver.forms import TripCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from userAccount.models import User
# Create your views here.
@login_required
def StartJourney(request):
    if request.method=="POST":
        form=TripCreationForm(request.POST)
        user=get_object_or_404(User,pk=request.user.id)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.Driver=user
            trip.save()
            return redirect('home')
        else:
            return redirect('driver_start')
    form=TripCreationForm()
    context={'form':form}
    return render(request,'driver/startJourney.html',context)
