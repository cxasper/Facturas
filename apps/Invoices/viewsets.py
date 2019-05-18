# apps/Invoices/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet


# Local imports
from .serializers import InvoicesSerializer, DetailInvoicesSerializer
from .models import Invoice, DetailInvoice


# Create your viewsets here.
class InvoicesViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoicesSerializer

class DetailInvoicesViewSet(ModelViewSet):
    queryset = DetailInvoice.objects.all()
    serializer_class = DetailInvoicesSerializer
