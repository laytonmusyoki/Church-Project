from django.urls import path
from .views import Register,signin


urlpatterns=[
    path('register/',Register,name='Register'),
    path('signin/',signin,name='signin')
]