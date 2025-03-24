from rest_framework import routers
from acompanhamento.api import viewsets
acompanhamento_router = routers.DefaultRouter()
acompanhamento_router.register('acompanhamento', viewsets.AcompanhamentoViewSet)