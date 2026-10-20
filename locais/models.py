from django.db import models

# Create your models here.

class LocalVacinacao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Local de Vacinação'
        verbose_name_plural = 'Locais de Vacinação'
        ordering = ['nome']

    def __str__(self):
        return self.nome
