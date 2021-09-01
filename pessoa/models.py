from django.db import models
from datetime import datetime
from garagem.models import Garagem

#class Pessoa(models.Model):
#    nome = models.CharField(max_length=1000)
#    telefone = models.IntegerField()
#    email = models.CharField(max_length=500)
#    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)
#    visivel = models.BooleanField(default=True)
    
#    def __str__(self):
#        return self.nome

class Pessoa(models.Model):
    
    nome = models.CharField(max_length=1000)
    telefone = models.IntegerField(unique=True)
    email = models.EmailField(blank=False, unique=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)
    visivel = models.BooleanField(default=True)
