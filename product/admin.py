from django.contrib import admin
from product.models import Product,Category,CategoryDetail,Review,ProductImage

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(CategoryDetail)
admin.site.register(Review)
