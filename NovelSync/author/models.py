from django.db import models
from django.contrib.auth.models import User
import uuid

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class AuthorProfile(models.Model):
    author_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author_name = models.OneToOneField(User, on_delete=models.CASCADE)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    author_img = models.ImageField(upload_to="author_profile/")
    author_mob = models.CharField(max_length=10, null=True, unique=True)
    author_email = models.CharField(max_length=100, null=True, unique=True)
    author_education = models.CharField(max_length=100, null=True)
    author_books = models.CharField(max_length=100, unique=True, null=True, blank=True)
    author_about = models.TextField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.author_name)  