from django.contrib import admin
from all_students.models import Student_registration

# Register your models here.
class Student_Admin(admin.ModelAdmin):
  list_display =['stu_img','stu_id','stu_name','stu_roll','stu_mob','stu_clg_name','stu_description']
admin.site.register(Student_registration,Student_Admin)

