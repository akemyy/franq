from django.db import models
from datetime import datetime

class Veiculo(models.Model):
    tipo = {
        ('M', 'Moto' ),
        ('C', 'Carro' )
    }
    tipo = models.CharField(max_length=1, choices=tipo, blank=False, null=False)
    modelo = models.CharField(max_length=200, blank=True)
    ano_veiculo = models.IntegerField()
    cor = models.CharField(max_length=200, blank=True)
    placa = models.CharField(max_length=10, blank=False, null=False)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)
    visivel = models.BooleanField(default=True)
    def __str__(self):
        return self.placa
    class Meta:
        ordering = ['placa']

class Garagem(models.Model):
    
    ativa = models.BooleanField(default=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, blank=True, null=True)
    telefone = models.IntegerField()
    email = models.CharField(max_length=500)
    def __str__(self):
        return self.id
    