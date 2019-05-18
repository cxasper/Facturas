# apps/products/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Product


# Create your serializers here.
class ProductsSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
