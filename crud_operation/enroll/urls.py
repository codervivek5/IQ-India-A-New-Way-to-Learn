from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   # Student path
   path('', views.home, name='home'),
   path('add-student/', views.add_student, name='add_student'),
   path('update-student/', views.update_student, name='update_student'),
   path('all-student/', views.all_student, name='all_student'),
   path('register-student/', views.register_student, name='register_student'),
   path('view-data/', views.view_data, name='view_data'),
   
   # Admin path
   path('login/', views.login_admin, name='login_admin'),
   path('register/', views.register_admin, name='register_admin'),
   path('logout/', views.user_logout, name='logout'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
