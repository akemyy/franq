from django.db import models
from datetime import datetime


class Pessoa(models.Model):
    nome = models.CharField(max_length=1000)
    telefone = models.IntegerField()
    email = models.CharField(max_length=500)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)
    visivel = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
    
class Veiculo(models.Model):
    tipo = {
        ('M', 'Moto' ),
        ('C', 'Carro' )
    }
    tipo = models.CharField(max_length=1, choices=tipo, blank=False, null=False)
    modelo = models.CharField(max_length=200, blank=True)
    ano_veiculo = models.IntegerField()
    cor = models.CharField(max_length=200, blank=True)
    placa = models.CharField(max_length=10, blank=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)
    visivel = models.BooleanField(default=True)
    def __str__(self):
        return self.placa
    
    
class Garagem(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    ativa = models.BooleanField(default=True)
