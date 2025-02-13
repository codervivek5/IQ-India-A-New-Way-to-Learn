from django.db import models #type: ignore

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
    roll_number = models.IntegerField(unique=True)  
    phone_number = models.IntegerField()
    college = models.CharField(max_length=50, null=True, blank=True)  
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='student_photos/')
    student_desc = models.TextField(max_length=300)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_name       
    
    
