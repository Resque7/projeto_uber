from django.db import models
from .const import COLORS
from usuarios.models import Usuario


class Marca(models.Model):
    nome = models.CharField(max_length=70, null=False, blank=False)


class Veiculo(models.Model):
    placa = models.CharField(max_length=7, null=False, blank=False)
    modelo = models.CharField(max_length=128, null=False, blank=False)
    cor = models.SmallIntegerField(choices=COLORS, null=False, blank=False, default=1)
    marca = models.ForeignKey(Marca, related_name='veiculos', on_delete=models.PROTECT)
    ativo = models.BooleanField(default=True)
    proprietario = models.ForeignKey(Usuario, related_name='veiculos', on_delete=models.PROTECT, null=False, blank=False)

