from rest_framework import viewsets
from nutricionista import models
from nutricionista.api import serializers
class NutricionistaViewSet(viewsets.ModelViewSet):
    queryset = models.Nutricionista.objects.all()
    serializer_class = serializers.NutricionistaSerializer