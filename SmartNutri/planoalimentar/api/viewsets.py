from rest_framework import viewsets
from planoalimentar import models
from planoalimentar.api import serializers
class PlanoalimentarViewSet(viewsets.ModelViewSet):
    queryset = models.Receita.objects.all()
    serializer_class = serializers.PlanoalimentarSerializer