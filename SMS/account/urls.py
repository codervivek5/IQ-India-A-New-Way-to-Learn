from django.urls import path  # type: ignore
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),  # Renamed function
]
