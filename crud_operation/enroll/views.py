from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render( request, "enroll/home.html")

def update_student(request):
    return render( request, "enroll/update_std.html")

def add_student(request):
    return render( request, "enroll/add_std.html")

def all_student(request):
    return render( request, "enroll/all_students.html")

def view_data(request):
    return render( request, "enroll/view_data.html")

def register_student(request):
    return HttpResponse("this is the page belong to register students")

def login_admin(request):
    return render( request, "enroll/login.html")

def register_admin(request):
    return render( request, "enroll/register_admin.html")

def user_logout(request):
    pass


