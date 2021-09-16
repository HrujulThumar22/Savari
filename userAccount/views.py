from django.shortcuts import render,HttpResponse
from userAccount.forms import RegisterForm,UpdateForm
from django.contrib import messages

from .models import User
# Create your views here.
def home(request):
    return HttpResponse("Home Page")

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

def updateUser(request,pk):
    user=User.objects.get(id=pk)
    form=UpdateForm(instance=user)
    print(form)
    if request.method=="POST":
        form=UpdateForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse("hi")
        else:
            context={'form':form}
            messages.error(request,'There is Error in your information...kindly refill the form')
            render(request,'userAccount/update.html',context)
    context={'form':form}
    return render(request,'userAccount/update.html',context)