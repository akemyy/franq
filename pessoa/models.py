from django.db import models
from datetime import datetime


class Pessoa(models.Model):
    nome = models.CharField(max_length=1000)
    telefone = models.IntegerField()
    email = models.CharField(max_length=500)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)
    visivel = models.BooleanField(default=True)