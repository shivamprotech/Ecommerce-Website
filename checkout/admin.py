from django.contrib import admin
from checkout.models import Cart,CartDetail,Order,OrderDetail

# Register your models here.

admin.site.register(Cart)
admin.site.register(CartDetail)
admin.site.register(Order)
admin.site.register(OrderDetail)
