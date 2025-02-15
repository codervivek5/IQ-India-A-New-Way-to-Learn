from django import forms  #type: ignore
from .models import Employee, Qualification

class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_name', 'emp_profile', 'emp_qualification', 'emp_mobile_no', 
                  'emp_salary', 'emp_email', 'emp_experience']
    
    # Custom Validations
    emp_mobile_no = forms.CharField(
        max_length=10,
        min_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter 10-digit mobile number'})
    )
    emp_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter valid email'})
    )
    emp_salary = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter salary'})
    )
    emp_experience = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter years of experience'})
    )

    # Styling Fields with Bootstrap
    def __init__(self, *args, **kwargs):
        super(EmployeeRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
