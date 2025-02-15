from django.urls import path  #type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-emp/', views.all_emp, name='all_emp'),
    path('add-emp/', views.add_emp, name='add_emp'),
    path('employee-details/<uuid:emp_id>/', views.employee_detail, name='employee_detail'),
    


    path('login/', views.login, name='login'),
    path('signup/', views.sign_up, name='sign_up'),



]


