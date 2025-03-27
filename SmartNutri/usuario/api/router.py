from rest_framework import routers
from usuario.api import viewsets

usuario_router = routers.DefaultRouter()
usuario_router.register('usuario', viewsets.UsuarioViewSet)