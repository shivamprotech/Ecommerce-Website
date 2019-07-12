from django.db import models
from account.models import Customer
from product.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'customer_cart',default='')
    total_price = models.FloatField()

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='customer_cart_detail')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_product')

class Order(models.Model):
    STATUS = (('Received','R'), ('Processed','P'), ('Dispatch','D'), ('Fulfilled','F'))
    date = models.DateField(null=True)
    amount = models.FloatField(null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer_order')
    status = models.CharField(max_length=1,choices=STATUS)

class OrderDetail(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='customer_oder_detail')
    quantity = models.PositiveIntegerField()