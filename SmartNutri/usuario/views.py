from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from api.serializers import LoginSerializer, SignUpSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.validated_data['usuario']

        return Response({
            'nome': usuario.nome,
            'email': usuario.email,
        }, status=status.HTTP_200_OK)
        
class SignupView(generics.CreateAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()

        return Response({
            'nome': usuario.nome,
            'email': usuario.email,
        }, status=status.HTTP_201_CREATED)