from decorators.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from driver.forms import TripCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from passengerTrip.models import UserTrip
from userAccount.models import User
from .models import DriverTrip
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView 
from django.contrib.auth import get_user_model
from notifications.signals import notify

UserModel = get_user_model()
# Create your views here.
@login_required
@allowed_users(allowed_role=['Driver'])
def StartJourney(request):
    if request.method=="POST":
        form=TripCreationForm(request.POST,request.FILES)
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
@allowed_users(allowed_role=['Driver'])
def Home(request):
    trips=DriverTrip.objects.filter(Driver_id=request.user.id)
    if trips.exists():
        context={'trips':trips}
    else:
        context={'trips':False}
    return render(request,'driver/home.html',context)

def RideRequest(request):
    myRideRequest=UserTrip.objects.filter(trip__Driver=request.user)
    context={'rideRequest':myRideRequest}
    return render(request,'driver/rideRequest.html',context)

def acceptRequest(request,pk):
    rideRequest=UserTrip.objects.filter(pk=pk)
    rideRequest.requestStatus=1
    sender = UserModel.objects.get(username=request.user)
    recipient = UserModel.objects.get(pk=rideRequest.passenger.id)
    message = "Your request for the ride is Accepted."
    notify.send(sender, recipient=recipient, verb='Message',description=message)
    return redirect('driver_request')

def rejectRequest(request,pk):
    rideRequest=UserTrip.objects.filter(pk=pk)
    rideRequest.requestStatus=2
    sender = UserModel.objects.get(username=request.user)
    recipient = UserModel.objects.get(pk=rideRequest.passenger.id)
    message = "Your request for the ride is Rejected."
    notify.send(sender, recipient=recipient, verb='Message',description=message)
    return redirect('driver_request')

class RideDetail(DetailView): 
    model = DriverTrip
    template_name="driver/ride_detail.html"
    context_object_name ="ride"