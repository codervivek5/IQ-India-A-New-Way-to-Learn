from account.views import *
from django.urls import path 

urlpatterns = [
    
    path('signup/',signup,name='signup')
]
