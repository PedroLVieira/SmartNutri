from rest_framework import routers
from substituicao.api import viewsets
substituicao_router = routers.DefaultRouter()
substituicao_router.register('substituicao', viewsets.SubstituicaoViewSet)