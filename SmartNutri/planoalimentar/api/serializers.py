from rest_framework import serializers
from planoalimentar import models

class PlanoalimentarSerializer(serializers.ModelSerializer):
   class Meta:
    model = models.PlanoAlimentar
    fields = '__all__'