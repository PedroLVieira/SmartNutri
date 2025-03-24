from rest_framework import viewsets
from receita import models
from receita.api import serializers
class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = models.Receita.objects.all()
    serializer_class = serializers.ReceitaSerializer