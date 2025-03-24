from rest_framework import viewsets
from ingrediente import models
from ingrediente.api import serializers
class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = models.Ingrediente.objects.all()
    serializer_class = serializers.IngredienteSerializer