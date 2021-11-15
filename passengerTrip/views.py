from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from django.contrib import messages
from decorators.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from driver.models import DriverTrip 
from .models import UserTrip
from passengerTrip.forms import BookRideForm, ConfirmRideForm

from notifications.signals import notify
UserModel = get_user_model()
# Create your views here.
@login_required
@allowed_users(allowed_role=['Passenger'])
def home(request):
    myTrips=UserTrip.objects.filter(passenger=request.user.id)
    context={'myTrips':myTrips}
    return render(request,'userTrip/home.html',context)
@login_required
@allowed_users(allowed_role=['Passenger'])
def bookRide(request):
    if request.method=="POST":
        form=BookRideForm(request.POST)
        if form.is_valid():
            S_City=form.cleaned_data.get('Starting_City')
            D_city=form.cleaned_data.get('Destination_City')
            result=DriverTrip.objects.filter(Starting_City__name=S_City,Destination_City__name=D_city,TripStatus=0)
            context={'result':result,'form':form}
            return render(request,'userTrip/bookRide.html',context)
        else:
            return redirect('driver_start')
    form=BookRideForm()
    context={'form':form}
    return render(request,'userTrip/bookRide.html',context)


@login_required
@allowed_users(allowed_role=['Passenger'])
def confirmRide(request,pk):
    tripDetails=get_object_or_404(DriverTrip,pk=pk)
    if request.method=="POST":
        form=ConfirmRideForm(request.POST)
        if form.is_valid():
            userTrip = form.save(commit=False)
            if(tripDetails.Vacancy>=userTrip.noOfSeatsBooked):
                userTrip.trip=tripDetails
                user=get_object_or_404(UserModel,pk=request.user.id)
                userTrip.passenger=user
                tripDetails.save()
                userTrip.save()
                sender = UserModel.objects.get(username=request.user)
                recipient = UserModel.objects.get(pk=tripDetails.Driver.id)
                message = "You Got request for your ride."
                notify.send(sender, recipient=recipient, verb='Message',description=message)
                return redirect('passenger_home')
            else :
                messages.error(request, str(userTrip.noOfSeatsBooked) + ' Seats not Available. Seats must not be greater the available seats')
        else:
            messages.error(request,'Please enter valid Detaild')
            return redirect('book_ride')
    form=ConfirmRideForm()
    context={'trip':tripDetails,'form':form}
    return render(request,'userTrip/confirmRide.html',context)