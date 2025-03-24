from rest_framework import routers
from nutricionista.api import viewsets
nutricionista_router = routers.DefaultRouter()
nutricionista_router.register('nutricionista', viewsets.NutricionistaViewSet)