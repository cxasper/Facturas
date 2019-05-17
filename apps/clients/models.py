# apps/clients/models.py
# Python imports


# Django imports
from django.db import models

# Third party apps imports


# Local imports


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    dni = models.CharField(max_length=8)
    phone = models.CharField(max_length=9)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)
