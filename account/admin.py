from django.contrib import admin
from account.models import CustomUser,Customer,Seller
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):

    fields = ('username','first_name','last_name','email','password','date_of_birth','phone_number','gender','address')

    exclude = ('is_staff','date_joined','groups')

class SellerAdmin(admin.ModelAdmin):

    fields = ('username','first_name','last_name','email','password','date_of_birth','phone_number','gender','address','document')

    exclude = ('is_staff','date_joined','groups')

admin.site.register(CustomUser)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Seller,SellerAdmin)