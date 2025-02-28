from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request, "author_login.html")

def author_signup(request):
    return render(request, "author_signup.html")

def author_login(request):
    return render(request, "author_login.html")