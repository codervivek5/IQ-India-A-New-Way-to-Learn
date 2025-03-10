from django.urls import path  #type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-emp/', views.all_emp, name='all_emp'),
    path('add-emp/', views.add_emp, name='add_emp'),
    path('employee-details/<uuid:emp_id>/', views.employee_detail, name='employee_detail'),
    path('edit-employee/<uuid:emp_id>/', views.edit_employee, name='edit_employee'),
    path('delete-employee/<uuid:emp_id>/', views.delete_employee, name='delete_employee'),

    path('login/', views.login_view, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path('signup/', views.sign_up, name='sign_up'),



]


