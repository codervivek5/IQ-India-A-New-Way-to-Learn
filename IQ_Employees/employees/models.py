from django.db import models #type: ignore
import uuid

# Create your models here.

class Qualification(models.Model):
    qualification = models.CharField(max_length=20)
    
    def __str__(self):
        return self.qualification
     

class Employee(models.Model):
    emp_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    emp_name = models.CharField(max_length=50)
    emp_profile = models.CharField(max_length=20)
    emp_qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    emp_mobile_no = models.CharField(max_length=10, unique=True)
    emp_salary = models.PositiveIntegerField()
    emp_email = models.EmailField(max_length = 254, unique=True)
    emp_experience = models.PositiveIntegerField()
    
    def __str__(self):
        return self.emp_name
    

    
        
    
