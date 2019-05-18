# apps/products/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Product


# Register your models here.
@admin.register(Product)
class ProductsModelAdmin(admin.ModelAdmin):
    pass
