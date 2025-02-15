from django.shortcuts import render,redirect, HttpResponse #type: ignore
from .models import *
from django.shortcuts import render, get_object_or_404 #type: ignore
from .forms import EmployeeRegistrationForm
from django.contrib import messages #type: ignore
 
# Create your views here.
def home(request):
    return render(request, "home.html")
    # return HttpResponse("this is home page")

def all_emp(request):
    employees = Employee.objects.all()
    return render(request, "all_emp.html",{'employees':employees})


def employee_detail(request,emp_id):
    # employees = Employee.objects.all()
    employee = get_object_or_404(Employee, emp_id=emp_id)
    return render(request, "employee_detail.html",{'employee':employee})

def add_emp(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)   
        
        emp_email = Employee.objects.filter(emp_mobile_no = request.POST.get('emp_mobile_no')).exists()
        email_exits = Employee.objects.filter(emp_email = request.POST.get('emp_email')).exists()
        
        if emp_email :
            messages.error(request, "Employee with this Mobile Number already exists!")           
        elif email_exits:
            messages.error(request, "Employee with this Email already exists!")  
                 
        elif form.is_valid():
            form.save()
            messages.success(request, "Employee Registered Successfully !")
            return redirect("home")
        else:
            print(form.errors)
    else:
        form = EmployeeRegistrationForm()
    return render(request, "add_emp.html", {'form':form})


def login(request):
    return render(request, "login.html")


def sign_up(request):
    return render(request, "sign_up.html")
    
