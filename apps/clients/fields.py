# apps/clients/fields.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import PrimaryKeyRelatedField


# Local imports
from .models import Client
from .serializers import ClientsSerializer


# Create your serializers here.
class ClientsField(PrimaryKeyRelatedField):
    queryset = Client.objects.all()

    def to_representation(self, value):
        instance = self.get_queryset().get(pk=value.pk)
        serializer = ClientsSerializer(instance)
        return serializer.data
