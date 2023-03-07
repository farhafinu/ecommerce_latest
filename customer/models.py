from email.policy import default
from django.db import models
from datetime import date
from reseller_app.models import Product


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=200,default="")

class AddCart(models.Model):
    product  = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    qty = models.IntegerField(default=1)

    def __str__ (self):
        return 'MyClass(x=' + AddCart.product + ' ,y=' + AddCart.qty + ')'




class Order(models.Model):
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    status = models.CharField(max_length=20,default="pending")
    provider_order_id = models.CharField( max_length=40,default='' )
    payment_id = models.CharField(max_length=36,default='')
    signature_id = models.CharField(max_length=128,default='' )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"



class Order_detail(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField()
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=20,default="order placed") #update after payment confirmed
    payment_type = models.CharField(max_length=20,default='')
    order=models.ForeignKey(Order,on_delete=models.CASCADE,default=0)
 



