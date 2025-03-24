from rest_framework import routers
from cliente.api import viewsets
cliente_router = routers.DefaultRouter()
cliente_router.register('cliente', viewsets.ClienteViewSet)