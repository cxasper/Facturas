# apps/clients/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import ClientsViewSet


# Create your routers here.
clients = (
    (r'clients', ClientsViewSet),
)
