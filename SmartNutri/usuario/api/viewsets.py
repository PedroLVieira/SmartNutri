from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import permissions

from usuario import models
from usuario.api import serializers


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class SignUpView(generics.CreateAPIView):
    serializer_class = serializers.SignUpSerializer
    
    def post(self, request: Request):
        data = request.data()
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            response={
                "message": "Usuário criado com sucesso.",
                "data": serializer.data
            }
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)