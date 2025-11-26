# Ex01 Django ORM Web Application
## Date: 26.11.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
```
models.py
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


admin.py
from django.contrib import admin
from .models import Student,StudentAdmin

# Register your models here.
admin.site.register(Student, StudentAdmin)

```
## OUTPUT
![alt text](<Screenshot (23).png>)
![alt text](<Screenshot (24).png>)
![alt text](<Screenshot (25).png>)



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
