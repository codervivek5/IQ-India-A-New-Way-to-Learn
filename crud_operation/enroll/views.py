from django.shortcuts import render, redirect  # type: ignore
from .forms import StudentForm  # Import the form used for student registration
from django.contrib.auth import authenticate, login, logout  # type: ignore
from django.contrib import messages  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from .models import Student

# Home view, renders the home page
def home(request):
    return render(request, "enroll/home.html")

# Update student view, renders the update student page
def update_student(request):
    return render(request, "enroll/update_std.html")

# Add student view, renders the add student page
def add_student(request):
    return render(request, "enroll/add_std.html")

# All students view, renders the page showing all students
def all_student(request):
    students = Student.objects.all() 
    # print(students)
    return render(request, "enroll/all_students.html",{'students':students})

# View data page, renders the page for viewing student data
def view_data(request):
    students = Student.objects.all() 
    print(students)
    return render(request, "enroll/view_data.html")

# Register a new student
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  # Handle both POST data and file uploads
        if form.is_valid():
            form.save()  # Save the student data to the database
            print('form save', form)
            return redirect('all_student')  # Redirect to the all students page after successful registration
        else:
            form = StudentForm()  # Initialize the form for GET requests
   #  return render(request, "enroll/std_registration.html", {'form': form})  # Render the registration page with the form
    return render(request, "enroll/std_registration.html")  # Render the registration page with the form

# Admin login view
def login_admin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        # Authenticate the user with the provided credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log in the user
            messages.success(request, "Login successfully!")  # Success message
            return redirect("all_student")  # Redirect to the all students page after successful login
        else:
            messages.error(request, "Invalid Credentials")  # Error message if authentication fails
    
    return render(request, "enroll/login.html")  # Render the login page

# Register an admin user view
def register_admin(request):
    if request.method == 'POST':
        name = request.POST.get('name', "").strip()
        username = request.POST.get('username', "").strip()
        password = request.POST.get('password', "").strip()
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists!")  # Error message if username is already taken
            return redirect("register_admin")
        
        # Create a new user and assign the name
        user = User.objects.create_user(username=username, password=password)
        user.first_name = name  # Assign the first name to the new user
        user.save()  # Save the new user to the database
        messages.success(request, "Registered Successfully!")  # Success message
        return redirect("login_admin")  # Redirect to the login page after successful registration
    
    return render(request, "enroll/register_admin.html")  # Render the register admin page

# Logout the user
def user_logout(request):
    logout(request)  # Log out the current user
    messages.success(request, "Logout Successfully!")  # Success message
    return redirect("login_admin")  # Redirect to the login page after logout
