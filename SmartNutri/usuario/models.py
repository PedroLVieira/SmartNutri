from django.db import models

class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    
    TIPO_USUARIO = [
        ('cliente', 'Cliente'),
        ('nutricionista', 'Nutricionista'),
    ]
    tipo = models.CharField(max_length=15, choices=TIPO_USUARIO)

    def __str__(self):
        return self.nome
