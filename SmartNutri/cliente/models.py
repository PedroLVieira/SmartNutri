from django.db import models
from usuario.models import Usuario

class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    
    SEXO_CHOICES = [('M', 'Masculino'), ('F', 'Feminino')]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    
    altura = models.DecimalField(max_digits=4, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    objetivo = models.TextField()

    def __str__(self):
        return self.usuario.nome
