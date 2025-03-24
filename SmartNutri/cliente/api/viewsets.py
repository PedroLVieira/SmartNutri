from rest_framework import viewsets
from cliente import models
from cliente.api import serializers
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer