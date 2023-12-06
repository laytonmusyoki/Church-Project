from django.urls import path
from .views import youths,profile,contact,sermons,Youth_fellowship,Church_Outreach,Spiritual_Growth

urlpatterns = [
    path('youths/',youths, name='youths'),
    path('profile/',profile, name='profile'),
    path('contact/',contact, name='contact'),
    path('sermons/',sermons, name='sermons'),
    path('Youth_fellowship/',Youth_fellowship, name='Youth_fellowship'),
    path('Church_Outreach/',Church_Outreach, name='Church_Outreach'),
    path('Spiritual_Growth/',Spiritual_Growth, name='Spiritual_Growth'),
]