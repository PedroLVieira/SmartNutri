from rest_framework import routers
from ingrediente.api import viewsets
ingrediente_router = routers.DefaultRouter()
ingrediente_router.register('ingrediente', viewsets.IngredienteViewSet)