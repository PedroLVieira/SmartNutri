from django.db import models

class Receita(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    calorias = models.DecimalField(max_digits=6, decimal_places=3)
    proteinas = models.DecimalField(max_digits=6, decimal_places=3)
    carboidratos = models.DecimalField(max_digits=6, decimal_places=3)
    gorduras = models.DecimalField(max_digits=6, decimal_places=3)
# Create your models here.
