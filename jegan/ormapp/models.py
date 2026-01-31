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