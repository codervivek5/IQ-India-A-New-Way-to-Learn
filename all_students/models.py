from django.db import models
import random as rd 
import string as st

# Create your models here.
s_id = lambda: "ID"+''.join(rd.choices(st.digits,k=10))
class Student_registration(models.Model):
  
  stu_img= models.ImageField(upload_to='uploads/')
  stu_id= models.CharField(max_length=12,default=s_id())
  stu_name= models.CharField(max_length=20,default='NA')
  stu_roll= models.CharField(max_length=10)
  stu_mob = models.BigIntegerField()
  stu_clg_name = models.CharField(max_length=200) 
  stu_description = models.TextField() 
  
   
  
  def __str__(self):
    return f"{self.stu_name}"
  