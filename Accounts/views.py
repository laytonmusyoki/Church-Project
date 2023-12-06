from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def Register(request):
    form=RegistrationForm
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully for {username}')
            return redirect('signin')
    context={
        'forms':form
    }
    return render(request,'register.html',context)


def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,f'Welcome {username} to Eaglerise Community')
            return redirect('youths')
        else:
            messages.warning(request,'Wrong credentials')
            return redirect('signin')
    return render(request,'login.html')





def signout(request):
    logout(request)
    messages.warning(request,'You have been logged out')
    return redirect('index')


