from rest_framework import viewsets
from acompanhamento import models
from acompanhamento.api import serializers
class AcompanhamentoViewSet(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.AcompanhamentoSerializer