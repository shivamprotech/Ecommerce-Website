from django.db import models
from account.models import Customer

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=64)
    cost = models.IntegerField()
    description = models.CharField(max_length=400)
    stock = models.PositiveIntegerField()

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='images/')

class Category(models.Model):
    name = models.CharField(max_length=64)
    
class CategoryDetail(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    category_description = models.CharField(max_length=400)

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

class ReviewDetail(models.Model):
    review = models.ForeignKey(Review,on_delete=models.CASCADE)
    review_description = models.CharField(max_length=400)
    date = models.DateField(null=True)


