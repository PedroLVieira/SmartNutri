from rest_framework import viewsets
from usuario import models
from usuario.api import serializers

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer