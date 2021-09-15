from django.shortcuts import render,HttpResponse
from userAccount.forms import RegisterForm
# Create your views here.
def driverSignup(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        print(request.POST['dob'])
        if form.is_valid():
            form.save()
            return HttpResponse("hi")
        else:
            context={'form':form}
            render(request,'userAccount/signup.html',context)
    form=RegisterForm()
    for field in form:
        print(field)
    context={'form':form}
    return render(request,'userAccount/signup.html',context)
