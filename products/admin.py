from django.contrib import admin
from .models import Product, Buy

class BuyAdmin(admin.ModelAdmin):
    list_display = ("name", "stock")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")

admin.site.register(Buy, BuyAdmin)
admin.site.register(Product, ProductAdmin)
