from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        
        name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter full name: "}))
        
        roll_number = forms.IntegerField(widget=forms.NumberInput({
            "class":"form-control",
            "placeholder":"Enter your roll no: "
        }))
        branch = forms.CharField(widget=forms.BooleanField)
        
        model = Student
        fields = "__all__"  # Include all model fields in the form
