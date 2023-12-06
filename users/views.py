from django.shortcuts import render
from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings


def index(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        message=request.POST['message']
        subject='People Enquiries'
        context={
            'name':fname,
            'email':email,
            'message':message
        }
        html_message = render_to_string('email_template.html', context)
        try:
            email = EmailMultiAlternatives(
                subject, 
                message, 
                email,  
                [settings.RECIPIENT_EMAIL],  
                reply_to=[email], 
            )
            email.attach_alternative(html_message, "text/html")
            email.send()
            messages.success(request,f'Dear , {fname} {lname} we have received your message and we will get back to you shortly')
        except Exception as e:
            print(e)
            messages.warning(request,'Please check your internet and try again')
    return render(request, "index.html")




    
