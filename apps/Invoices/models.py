# apps/Invoices/models.py
# Python imports


# Django imports
from django.db import models
from django.core.validators import MinValueValidator
# Third party apps imports

# Local imports
from apps.clients.models import Client
from apps.products.models import Product
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

    total = models.CharField(max_length=55, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)

class DetailInvoice(models.Model):
    invoice_id = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(Product)
    amount = models.FloatField(
        validators=[MinValueValidator(0.0)])
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)
