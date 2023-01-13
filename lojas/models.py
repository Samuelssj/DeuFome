from django.db import models
from django.contrib.auth.models import User


class Loja(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=255, blank=True)
    nome = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(blank=True)
    cnpj = models.CharField(max_length=255, blank=True)
    tipo = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nome
