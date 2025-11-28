from django.db import models
from django.contrib import admin

class Employee(models.Model):
    first_name = models.CharField(max_length=30, help_text='Enter First Name')
    last_name = models.CharField(max_length=30, help_text='Enter Last Name')
    phone_number = models.CharField(max_length=15, help_text='Enter Phone Number')
    date_of_birth = models.DateField()
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'date_of_birth')
    
# Create your models here.
