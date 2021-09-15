from django.shortcuts import render,HttpResponse
from userAccount.forms import RegisterForm
from django.contrib import messages
# Create your views here.
def driverSignup(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("hi")
        else:
            context={'form':form}
            messages.error(request,'There is Error in your information...kindly refill the form')
            render(request,'userAccount/signup.html',context)
    form=RegisterForm()
    context={'form':form}
    return render(request,'userAccount/signup.html',context)
