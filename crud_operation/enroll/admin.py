from django.contrib import admin  #type: ignore
from .models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Branch)
admin.site.register(Course)

