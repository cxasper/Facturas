# apps/Invoices/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import InvoicesViewSet, DetailInvoicesViewSet


# Create your routers here.
Invoices = (
    (r'invoices', InvoicesViewSet),
    (r'invoices/(?P<invoice_id>\d+)/details', DetailInvoicesViewSet),
)
