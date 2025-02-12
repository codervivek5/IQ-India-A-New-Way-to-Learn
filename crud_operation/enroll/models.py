from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=10)
    def __str__(self):
        return self.course_name
    
class Branch(models.Model):
    branch_name = models.CharField(max_length=10)
    def __str__(self):
        return self.branch_name

class Student(models.Model):
    student_name = models.CharField(max_length=30)
    # course = models.fore(max_length=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # branch = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch,  on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='student_photos/')
    roll_number = models.IntegerField()
    phone_number = models.IntegerField()
    student_desc = models.TextField(max_length=300)
    
    def __str__(self):
        return self.student_name        
    
    
