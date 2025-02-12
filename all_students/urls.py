from django.urls import path  # type: ignore
from all_students.views import*

urlpatterns = [
  path('', home, name = 'home'), 
  path("all_students/",all_students,name = "all_students"),
  path("stu_reg/",stu_reg,name='stu_reg'),
  path("delete_stu/<int:id>",delete_stu,name = "delete_stu"),
  # path("404/",error_404,name = "error404"),
  path("stu_details/<int:id>",stu_details,name="stu_details"),
  path("stu_update/<int:id>",update_student,name="stu_update")
]
