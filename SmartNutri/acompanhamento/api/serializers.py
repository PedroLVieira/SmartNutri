from rest_framework import serializers
from acompanhamento import models

class AcompanhamentoSerializer(serializers.ModelSerializer):
   class Meta:
    model = models.Acompanhamento
    fields = '__all__'