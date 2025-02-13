from django.shortcuts import render,redirect
from .forms import StudentForm

# Create your views here.
def student_registration(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)  # Handle form data
        if form.is_valid():
            form.save()  # Save to database
            return redirect("student_register")  # Redirect to success page
    else:
        form = StudentForm()  # Empty form for GET request
    
    return render(request, "demo.html", {"form": form})