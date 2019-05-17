# apps/clients/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Client


# Create your serializers here.
class ClientsSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
