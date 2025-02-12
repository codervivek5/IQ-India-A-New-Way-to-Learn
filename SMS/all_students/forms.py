from all_students.models import*
from django import forms


class Stu_reg_forms(forms.ModelForm):
  class Meta:
    model = Student_registration
    fields = '__all__'
     
    labels = {"stu_img": 'Uplode Photo',
              "stu_id":"Student ID",
              "stu_name": 'Student Name',
              "stu_roll": 'Student Roll',
              "stu_mob": 'Student Mobile',
              "stu_clg_name": 'Collage Name',
              "stu_description": 'massage'
              
              }
    
    
    widgets = {
      
      
      "stu_id":forms.TextInput(attrs={"placeholder":"Enter Your id",'class':'form-control w-100'}),
    
      "stu_name":forms.TextInput(attrs={"placeholder":"Enter Your Name",'class':'form-control w-100'}),
      "stu_roll":forms.TextInput(attrs={"placeholder":"Enter Your Roll Nuber ",'class':'form-control w-100'}),
      "stu_mob":forms.TextInput(attrs={"placeholder":"Enter Your Mobile  ",'class':'form-control w-100'}),
      
      "stu_clg_name":forms.TextInput(attrs={"placeholder":"Enter Your Collage name",'class':'form-control w-100'}),
      "stu_description":forms.Textarea(attrs={"placeholder":"massage here",'class':'form-control w-100'})
    }
   