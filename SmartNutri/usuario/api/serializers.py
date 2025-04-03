from rest_framework import serializers
from rest_framework.validators import ValidationError
from usuario import models
from django.contrib.auth import authenticate


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

class LoginSerializer(serializers.Serializer):
    nome = serializers.CharField()
    senha = serializers.CharField()

    def validate(self, attrs):
        nome = attrs.get('nome')
        senha = attrs.get('senha')

        if nome and senha:
            user = authenticate(request=self.context.get('request'), nome=nome, senha=senha)
            if user:
                attrs['user'] = user
                return attrs
            raise serializers.ValidationError('Credenciais inválidas')
        raise serializers.ValidationError('Os campos "nome" e "senha" são obrigatórios')