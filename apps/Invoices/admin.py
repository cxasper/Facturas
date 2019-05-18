# apps/Invoices/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Invoice


# Register your models here.
@admin.register(Invoice)
class InvoicesModelAdmin(admin.ModelAdmin):
    pass
