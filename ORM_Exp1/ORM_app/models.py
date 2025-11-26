from django.db import models
from django.contrib import admin

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=20, help_text= "Enter Student Name")
    age = models.IntegerField(help_text="Enter Student Age")
    dob = models.DateField()
    reg_no =models.IntegerField(help_text="Enter the Registration Nimber")

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'age', 'dob', 'reg_no']