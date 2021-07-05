from django.contrib import admin
from serialcrud.models import Company, EmployeeModel

# Register your models here. crud
# admin.site.register(EmployeeModel)
# admin.site.register(Company)
class Employeeadmin(admin.ModelAdmin):
    list_display = ['emp_id','empname','Email','salary','company']

admin.site.register(EmployeeModel, Employeeadmin)
admin.site.register(Company)