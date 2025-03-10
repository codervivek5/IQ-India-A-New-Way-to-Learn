from django.shortcuts import render,redirect, HttpResponse #type: ignore
from .models import *
from django.shortcuts import render, get_object_or_404 #type: ignore
from .forms import EmployeeRegistrationForm
from django.contrib import messages #type: ignore
from django.contrib.auth import logout,authenticate,login #type: ignore
from django.contrib.auth.models import User #type: ignore
 
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

def edit_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('all_emp')  # Redirect to employee list
    else:
        form = EmployeeRegistrationForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    
    try:    
        if request.method == 'POST':  # Confirm before deleting
            employee.delete()
            return redirect('all_emp') 
        
    except Exception as e:
        print("error occured: ", e )
    
    print(employee.delete())
    return render(request, 'home.html', {'employee': employee})


def add_emp(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)   
        
        email_mo_no = Employee.objects.filter(emp_mobile_no = request.POST.get('emp_mobile_no')).exists()
        emp_email   = Employee.objects.filter(emp_email = request.POST.get('emp_email')).exists()
        
        if email_mo_no :
            messages.error(request, "Employee with this Mobile Number already exists!")  
                     
        elif emp_email:
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


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username") 
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, "Login Successful !")
            return redirect("home")
        else:
            return render(request,"login.html",{"error":"Invalid credantials"})
    return render(request, "login.html")

def logout_view(request): 
    logout(request)  
    messages.success(request, "You have been logged out.")
    return redirect("login")

def sign_up(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.warning(request,"User already exist !")
            return render(request,"sign_up.html")
        
        user = User.objects.create_user(username=username,password=password,first_name=name)
        user.save()

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user:
            return redirect("home")
        
    return render(request, "sign_up.html")