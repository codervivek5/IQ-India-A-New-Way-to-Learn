from django.contrib import admin #type: ignore
from .models import Employee, Qualification

# Employee Admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'emp_id',
        'emp_name',
        'emp_profile',
        'emp_qualification',
        'emp_mobile_no',
        'emp_salary',
        'emp_email',
        'emp_experience',  # This should be fine as it corresponds to the field in the Employee model
    )
    search_fields = ['emp_name', 'emp_email', 'emp_mobile_no']
    # list_filter = ['emp_qualification', 'emp_profile']


# Qualification Admin
@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ('qualification',)
    # search_fields = ['qualification']

