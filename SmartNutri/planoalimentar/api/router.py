from rest_framework import routers
from planoalimentar.api import viewsets
planoalimentar_router = routers.DefaultRouter()
planoalimentar_router.register('planoalimentar', viewsets.PlanoalimentarViewSet)