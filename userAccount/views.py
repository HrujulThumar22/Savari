from decorators.decorators import unauthenticated_user
from django.shortcuts import render,HttpResponse,redirect
from userAccount.forms import RegisterForm,UpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from .models import User
# Create your views here.
def home(request):
    return HttpResponse("Home Page")

@unauthenticated_user
def handleLogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect('home')
        else:
            messages.error(request,'invalid credentials')
            return redirect('user_login')
    
    return render(request,'userAccount/login.html')

@unauthenticated_user
def signup(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login')
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

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('home')
