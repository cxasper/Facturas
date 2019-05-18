# apps/products/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .serializers import ProductsSerializer
from .models import Product


# Create your viewsets here.
class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
