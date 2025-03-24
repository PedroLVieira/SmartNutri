from rest_framework import serializers
from ingrediente import models

class IngredienteSerializer(serializers.ModelSerializer):
   class Meta:
    model = models.Ingrediente
    fields = '__all__'