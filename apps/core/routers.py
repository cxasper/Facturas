# apps/core/routers.py
# Python imports


# Django imports


# Third party apps imports
from rest_framework.routers import DefaultRouter


# Local imports
# from ..app_django.routers import router_list as app_django_router
from apps.clients.routers import clients
from apps.products.routers import products
from apps.Invoices.routers import Invoices

# Create your routers here.
# routers_tuples = (app_django_router,)
routers_tuples = (clients, products, Invoices,)
routers_lists = sum(
    [list(router_tuple) for router_tuple in routers_tuples], [])

router = DefaultRouter()

for router_list in sorted(routers_lists):
    router.register(router_list[0], router_list[1], base_name=router_list[0])
