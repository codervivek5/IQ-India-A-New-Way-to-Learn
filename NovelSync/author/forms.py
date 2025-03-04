from django import forms
from author.models import AuthorProfile, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class AuthorProfileForm(forms.ModelForm):
    class Meta:
        model = AuthorProfile
        fields = "__all__"
        exclude = ['author_id'] # Excluding the author_id field as it is auto-generated
        widgets = {
            'author_name': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author_img': forms.FileInput(attrs={'class': 'form-control'}),
            'author_mob': forms.TextInput(attrs={'class': 'form-control'}),
            'author_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'author_education': forms.TextInput(attrs={'class': 'form-control'}),
            'author_books': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # Additional validation for the email to be unique
    def clean_author_email(self):
        email = self.cleaned_data.get('author_email')
        if AuthorProfile.objects.filter(author_email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    # Additional validation for mobile number to be unique
    def clean_author_mob(self):
        mobile = self.cleaned_data.get('author_mob')
        if AuthorProfile.objects.filter(author_mob=mobile).exists():
            raise forms.ValidationError("This mobile number is already in use.")
        return mobile
        
        


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
