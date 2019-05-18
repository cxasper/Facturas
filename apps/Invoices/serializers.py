# apps/Invoices/serializers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

# Local imports
from .models import Invoice, DetailInvoice


# Create your serializers here.
class DetailInvoicesSerializer(ModelSerializer):

    class Meta:
        model = DetailInvoice
        fields = '__all__'

class InvoicesSerializer(ModelSerializer):
    details = serializers.SerializerMethodField()

    def get_details(self, instance):
        details = DetailInvoice.objects.filter(invoice_id=instance.id)
        serializer = DetailInvoicesSerializer(details, many=True)
        return serializer.data

    class Meta:
        model = Invoice
        fields = '__all__'
