from django.db import models

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    calorias_por_grama = models.DecimalField(max_digits=6, decimal_places=3)
    proteinas_por_grama = models.DecimalField(max_digits=6, decimal_places=3)
    carboidratos_por_grama = models.DecimalField(max_digits=6, decimal_places=3)