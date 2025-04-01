from rest_framework import serializers
from rest_framework.validators import ValidationError
from usuario import models


class UsuarioSerializer(serializers.ModelSerializer):
   class Meta:
      model = models.Usuario
      fields = '__all__'
      
class SignUpSerializer(serializers.ModelSerializer):
   class Meta:
      model = models.Usuario
      fields = ['nome', 'email', 'senha', 'tipo']
   def validate(self, attrs):
      email_exist= models.Usuario.objects.filter(email=attrs['email']).exists()
      
      if email_exist:
         raise ValidationError("Email já cadastrado.")
      return super().validate(attrs)