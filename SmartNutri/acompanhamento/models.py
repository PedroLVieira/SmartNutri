from django.db import models
from cliente.models import Cliente

class Acompanhamento(models.Model):
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    peso_atual = models.DecimalField(max_digits=5, decimal_places=2)
    observacoes = models.TextField()
# Create your models here.
