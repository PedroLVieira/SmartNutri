from django.db import models
from usuario.models import Usuario

class Nutricionista(models.Model):
    nutricionista_id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    crn = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.nome
