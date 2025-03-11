from django.db import models
from ingrediente.models import Ingrediente

class Substituicao(models.Model):
    motivo = models.TextField()
    Ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
