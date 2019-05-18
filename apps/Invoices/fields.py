# apps/Invoices/fields.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.serializers import PrimaryKeyRelatedField


# Local imports
from .models import Invoice
from .serializers import InvoicesSerializer


# Create your serializers here.
class InvoicesField(PrimaryKeyRelatedField):
    queryset = Invoice.objects.all()

    def to_representation(self, value):
        instance = self.get_queryset().get(pk=value.pk)
        serializer = InvoicesSerializer(instance)
        return serializer.data
