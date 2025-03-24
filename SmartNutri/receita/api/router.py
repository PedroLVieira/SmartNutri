from rest_framework import routers
from receita.api import viewsets
receita_router = routers.DefaultRouter()
receita_router.register('receita', viewsets.ReceitaViewSet)