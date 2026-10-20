from django.db import models

from locais.models import LocalVacinacao
from vacinas.models import Vacina


# Create your models here.

class Campanha(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()

    vacinas = models.ManyToManyField(Vacina)
    locais = models.ManyToManyField(LocalVacinacao)

    class Meta:
        verbose_name = 'Campanha'
        verbose_name_plural = 'Campanhas'
        ordering = ['nome']

    def __str__(self):
        return self.nome