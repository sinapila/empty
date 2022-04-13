from django.contrib import admin

from . import models


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = [
        'is_active',
        'category'
    ]
    list_display = [
        'title',
        'is_active',
        'is_delete',
        'price'
    ]
    list_editable = [
        'is_active',
        'price'
    ]


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)
