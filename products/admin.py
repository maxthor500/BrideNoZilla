from django.contrib import admin
from .models import Product, Category, Inventory

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'inventory'
        'price',
        'rating',
        'image',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'name_product',
        'quantity',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Inventory, InventoryAdmin)
# admin.site.register(Review)