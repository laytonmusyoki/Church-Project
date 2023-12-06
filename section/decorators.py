from django.contrib import messages
from django.shortcuts import redirect



def loginrequired(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return view_func(request,*args,**kwargs)
        else:
            messages.warning(request,'Please login to explore more')
            return redirect('index')
    return wrapper_func