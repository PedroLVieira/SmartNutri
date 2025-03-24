from rest_framework import serializers
from receita import models

class ReceitaSerializer(serializers.ModelSerializer):
   class Meta:
    model = models.Receita
    fields = '__all__'