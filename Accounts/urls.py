from django.urls import path
from .views import Register,signin,signout


urlpatterns=[
    path('register/',Register,name='Register'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout')
]