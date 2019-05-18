# apps/Invoices/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer


# Local imports
from .models import Invoice


# Create your serializers here.
class InvoicesSerializer(ModelSerializer):

    class Meta:
        model = Invoice
        fields = '__all__'
