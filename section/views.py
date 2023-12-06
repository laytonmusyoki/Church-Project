from django.shortcuts import render,HttpResponse
from .decorators import loginrequired

# Create your views here.
def youths(request):
    return render(request,'NiceAdmin/index.html')

def profile(request):
    return render(request,'NiceAdmin/users-profile.html')


def contact(request):
    return render(request,'NiceAdmin/pages-contact.html')


def data(request):
    return render(request,'NiceAdmin/tables-data.html')

def general(request):
    return render(request,'NiceAdmin/tables-general.html')


@loginrequired
def sermons(request):
    return render(request,'NiceAdmin/sermons.html')


@loginrequired
def Youth_fellowship(request):
    return render(request,'NiceAdmin/youth_fellowship.html')

@loginrequired
def Church_Outreach(request):
    return render(request,'NiceAdmin/Church_Outreach.html')


@loginrequired
def Spiritual_Growth(request):
    return render(request,'NiceAdmin/Spiritual_Growth.html')
