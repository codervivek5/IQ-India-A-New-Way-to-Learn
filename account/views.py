from django.shortcuts import render # type: ignore

# Create your views here.
def user_signup(request):
  return render(request,'signup.html')

def user_login(request):
  return render(request,'login.html')
