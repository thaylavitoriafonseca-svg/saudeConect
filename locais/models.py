from django.db import models


class LocalVacinacao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Local de vacinação'
        verbose_name_plural = 'Locais de vacinação'

    def __str__(self):
        return self.nome