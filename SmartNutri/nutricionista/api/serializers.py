from rest_framework import serializers
from nutricionista import models

class NutricionistaSerializer(serializers.ModelSerializer):
   class Meta:
    model = models.Nutricionista
    fields = '__all__'