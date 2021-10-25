from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from django.contrib.auth import get_user_model
from driver.models import DriverTrip 

from passengerTrip.forms import BookRideForm
UserModel = get_user_model()
# Create your views here.
def home(request):
    return render(request,'userTrip/home.html')

def bookRide(request):
    if request.method=="POST":
        form=BookRideForm(request.POST)
        if form.is_valid():
            S_City=form.cleaned_data.get('Starting_City')
            D_city=form.cleaned_data.get('Destination_City')
            result=DriverTrip.objects.filter(Starting_City__name=S_City,Destination_City__name=D_city)
            context={'result':result,'form':form}
            return render(request,'userTrip/bookRide.html',context)
        else:
            return redirect('driver_start')
    form=BookRideForm()
    context={'form':form}
    return render(request,'userTrip/bookRide.html',context)

def confirmRide(request,pk):
    return HttpResponse(pk)