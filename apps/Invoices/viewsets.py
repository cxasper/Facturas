# apps/Invoices/viewsets.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

# Local imports
from .serializers import InvoicesSerializer, DetailInvoicesSerializer
from .models import Invoice, DetailInvoice
from apps.products.models import Product

# Create your viewsets here.
class InvoicesViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoicesSerializer

class DetailInvoicesViewSet(ModelViewSet):
    queryset = DetailInvoice.objects.all()
    serializer_class = DetailInvoicesSerializer

    def create(self, request, *args, **kwargs):
        request_copy = request.data.copy()
        if 'quantity' in request_copy and  'product_id' in request_copy:
            product = request_copy['product_id']
            price_product = Product.objects.get(pk=product).price
            quantity = int(request_copy['quantity'])
            amount = quantity * price_product
            print(request_copy)
            request_copy.update({ 'amount' : amount })
        serializer = self.get_serializer(data=request_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
