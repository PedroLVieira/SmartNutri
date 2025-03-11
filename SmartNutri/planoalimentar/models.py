from django.db import models
from receita.models import Receita
from ingrediente.models import Ingrediente
from cliente.models import Cliente
from nutricionista.models import Nutricionista

class PlanoAlimentar(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nutricionista = models.ForeignKey(Nutricionista, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    receitas = models.ManyToManyField(Receita)
    ingredientes = models.ManyToManyField(Ingrediente)
    observacoes = models.TextField()
# Create your models here.
