from datetime import date
from pyexpat import model
from django.db import models

# Create your models here.

class Reseller(models.Model):
    s_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=300)
    account_no = models.BigIntegerField()
    ifsc = models.CharField(max_length=50)
    s_acholdername = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    s_pic = models.ImageField(upload_to='reseller/')
    s_status = models.CharField(max_length=12,default="pending")

class Product(models.Model):
    p_category = models.CharField(max_length=40,default="")
    p_name = models.CharField(max_length=30)
    seller_id = models.ForeignKey(Reseller, on_delete = models.CASCADE)
    p_number = models.BigIntegerField()
    p_details = models.CharField(max_length=300)
    p_price = models.BigIntegerField()
    p_stock = models.FloatField(default=0)
    p_image = models.ImageField(upload_to='product/')
    date = models.DateField(default=date.today)
