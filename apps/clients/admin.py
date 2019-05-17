# apps/clients/admin.py
# Python imports


# Django imports
from django.contrib import admin


# Third party apps imports


# Local imports
from .models import Client


# Register your models here.
@admin.register(Client)
class ClientsModelAdmin(admin.ModelAdmin):
    pass
