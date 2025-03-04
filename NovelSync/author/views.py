from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm

# Create your views here.

def home(request):
    return render(request, "author_login.html")

def author_signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect("author_login")  # Change 'home' to your actual home page URL
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})

def author_login(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect("home")  # Change 'home' to your actual home page URL
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()
    return render(request, "author_login.html", {"form": form})

def author_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("author_login")  # Change 'login' to your actual login page URL