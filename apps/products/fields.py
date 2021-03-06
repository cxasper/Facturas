# apps/products/fields.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import PrimaryKeyRelatedField


# Local imports
from .models import Product
from .serializers import ProductsSerializer


# Create your serializers here.
class ProductsField(PrimaryKeyRelatedField):
    queryset = Product.objects.all()

    def to_representation(self, value):
        instance = self.get_queryset().get(pk=value.pk)
        serializer = ProductsSerializer(instance)
        return serializer.data
