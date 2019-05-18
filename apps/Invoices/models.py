# apps/Invoices/models.py
# Python imports


# Django imports
from django.db import models
from django.core.validators import MinValueValidator
# Third party apps imports

# Local imports
from apps.clients.models import Client

# Create your models here.
class Invoice(models.Model):
    client_id = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        null=True
    )
    date = models.DateField()
    address = models.CharField(max_length=55)
    serie = models.CharField(max_length=45)
    number = models.IntegerField(
        validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)
