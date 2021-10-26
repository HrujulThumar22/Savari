from django.http import HttpResponse
from django.shortcuts import redirect, render

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
            
        return view_func(request,*args,**kwargs)
        
    return wrapper_func

def allowed_users(allowed_role=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group in allowed_role:
                return view_func(request,*args,**kwargs)
            res=allowed_role[0]
            context={'res':res}
            return render(request,'userAccount/wronguser.html',context)
            #return HttpResponse('Not Allowed Please Login as valid User '+ allowed_role[0])
        return wrapper_func
    return decorator