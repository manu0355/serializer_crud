from django.db import models

# Create your models here.

class Company(models.Model):
    c_name= models.CharField(max_length=100)
    c_address = models.TextField(max_length=200)

    def __str__(self):
        return self.c_name


class EmployeeModel(models.Model):
    emp_id= models.IntegerField(primary_key=True)
    empname= models.CharField(max_length=20)
    Email= models.EmailField()
    salary= models.IntegerField()
    company= models.ForeignKey(Company, related_name='employee', on_delete=models.CASCADE,null=True)

    class Meta:
        db_table="employeetable"
    
    def __str__(self):
        return str(self.emp_id) +" "+ self.empname
