# apps/products/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import ProductsViewSet


# Create your routers here.
products = (
    (r'products', ProductsViewSet),
)
