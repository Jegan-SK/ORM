# Ex01 Django ORM Web Application
## Date: 31.01.2026

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin

class Swiggy_DB(models.Model):
    Order_No=models.IntegerField(primary_key=True);
    date=models.DateField();
    time=models.TimeField();
    address=models.CharField(max_length=100);
    food_name=models.CharField(max_length=50);
    Price=models.FloatField();
    Quantity=models.IntegerField();
    Mobile_No=models.IntegerField();
class Swiggy_DBAdmin(admin.ModelAdmin):
    list_display=['Order_No','date','time','address','Price','Quantity','Mobile_No'];

admin.py
from .models import Swiggy_DB,Swiggy_DBAdmin
from django.contrib import admin
admin.site.register(Swiggy_DB,Swiggy_DBAdmin)
```


## OUTPUT
![alt text](<Screenshot (93).png>)


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
