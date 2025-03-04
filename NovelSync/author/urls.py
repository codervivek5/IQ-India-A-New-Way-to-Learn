from django.urls import path
from author import views


urlpatterns = [
    path('', views.home, name='home'),
    path('author-signup', views.author_signup, name='author_signup'),
    path('author-login', views.author_login, name='author_login'),
    path('author-logout', views.author_logout, name='author_logout'),

  
  
]
