from decorators.decorators import unauthenticated_user,allowed_users
from django.shortcuts import render,HttpResponse,redirect
from userAccount.forms import RegisterForm,UpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate   
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model 
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from .models import User
UserModel = get_user_model()
# Create your views here.
@login_required
def home(request):
    return render(request,'userAccount/home.html')

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
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('userAccount/auth_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            context={'form':form}
            messages.error(request,'There is Error in your information...kindly refill the form')
            render(request,'userAccount/signup.html',context)
    form=RegisterForm()
    context={'form':form}
    return render(request,'userAccount/signup.html',context)

@login_required
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

@login_required
def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
