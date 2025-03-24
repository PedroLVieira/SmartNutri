from rest_framework import serializers
from substituicao import models

class SubstituicaoSerializer(serializers.ModelSerializer):
   class Meta:
    model = models.Substituicao
    fields = '__all__'