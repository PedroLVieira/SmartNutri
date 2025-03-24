from rest_framework import viewsets
from substituicao import models
from substituicao.api import serializers
class SubstituicaoViewSet(viewsets.ModelViewSet):
    queryset = models.Substituicao.objects.all()
    serializer_class = serializers.SubstituicaoSerializer