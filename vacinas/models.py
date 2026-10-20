from django.db import models

# Create your models here.

class Vacina(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    lote = models.CharField(max_length=50)
    tipo_dose = models.CharField(max_length=50)
    descricao = models.TextField()

    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering = ['nome']

    def __str__(self):
        return self.nome
