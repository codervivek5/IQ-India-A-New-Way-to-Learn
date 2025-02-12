from django import forms #type: ignore
from .models import Student, Course, Branch

class NameForm(forms.Form):
    std_name = forms.CharField(label="Your Name", max_length=30)
    roll_number = forms.IntegerField(label="Roll Number")
    phone_number = forms.IntegerField(label="Phone Number")
    college = forms.CharField(label="College Name", max_length=50)
    course = forms.ModelChoiceField(label="Course", queryset=Course.objects.all())
    branch = forms.ModelChoiceField(label="Branch", queryset=Branch.objects.all())
    photo = forms.ImageField(label="Upload Photo", required=False)
    student_desc = forms.CharField(label="Student Description", widget=forms.Textarea(attrs={"rows": 3}), max_length=300)

    