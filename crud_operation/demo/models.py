from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    branch = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='student_photos/')
    
    def __str__(self):
        return self.name
