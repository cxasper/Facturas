# apps/Invoices/routers.py
# Python imports


# Django imports


# Third party apps imports


# Local imports
from .viewsets import InvoicesViewSet


# Create your routers here.
Invoices = (
    (r'invoices', InvoicesViewSet),
)
