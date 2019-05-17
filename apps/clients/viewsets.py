# apps/clients/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .serializers import ClientsSerializer
from .models import Client


# Create your viewsets here.
class ClientsViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer
