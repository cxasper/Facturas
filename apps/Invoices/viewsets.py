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
        self.reduce_product(product, quantity)
        self.get_total(request_copy['invoice_id'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def reduce_product(self, product_id, quantity):
        product = Product.objects.get(pk=product_id)
        product_quantity = product.quantity
        product.quantity = product_quantity - quantity
        product.save()

    def get_total(self, invoice):
        invoices_details = DetailInvoice.objects.filter(invoice_id=invoice)
        total = 0
        for detail in invoices_details:
            total = total + detail.amount
        invoice = Invoice.objects.get(pk=invoice)
        invoice.total = total
        invoice.save()
