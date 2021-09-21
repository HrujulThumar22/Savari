from django.shortcuts import render

# Create your views here.
def StartJourney(request):
    return render(request,'driver/startJourney.html')
