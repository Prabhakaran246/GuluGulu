from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description','created_at')

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','product_image','vendor','description','original_price','selling_price','created_at')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)