# apps/products/models.py
# Python imports


# Django imports
from django.db import models
from django.core.validators import MinValueValidator
# Third party apps imports


# Local imports


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=45)
    price = models.FloatField(
        validators=[MinValueValidator(0.0)])
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)])

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('id',)
