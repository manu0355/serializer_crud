from django.contrib import admin
from serialcrud.models import Company, EmployeeModel

# Register your models here. crud
admin.site.register(EmployeeModel)
admin.site.register(Company)