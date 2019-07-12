from django.db import models
from product.models import Product

# Create your models here.

class WishList(models.Model):
    date = models.DateField(null=True)
    # name = models.CharField()

class WishListDetail(models.Model):
    wishlist = models.ForeignKey(WishList,on_delete=models.CASCADE,related_name='wishlistdetials')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='wishlistproduct')
