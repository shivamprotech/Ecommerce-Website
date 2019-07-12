from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):

    GENDER = (('M','Male'),('F','Female'))

    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=12)
    gender = models.CharField(max_length=1,choices=GENDER)
    address = models.CharField(max_length=64)
    
    class Meta:
        verbose_name = _('customuser')
        verbose_name_plural = _('customusers')


class Customer(CustomUser):

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customer')

    def __str__(self):
        return self.first_name


class Seller(CustomUser):

    document = models.CharField(max_length=64)
    
    class Meta:
        verbose_name = _('seller')
        verbose_name_plural = _('seller')

