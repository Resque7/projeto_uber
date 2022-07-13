
from django.db import models
from veiculos.models import Veiculo


class Carona(models.Model):
    cliente = models.CharField(max_length=70, null=False, blank=False)
    client_adress = models.CharField(max_length=280, null=False, blank=False)
    final_adress = models.CharField(max_length=280, null=False, blank=False)
    carro = models.ForeignKey(Veiculo, related_name='carona', on_delete=models.PROTECT, null=False, blank=False)
    distancia = models.FloatField(null=False, blank=False)
    valor = models.DecimalField(decimal_places=2, max_digits=5, null=False, blank=False)

    def calcular_valor(self):
        self.valor = self.distancia * 0.57

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.calcular_valor()
        super(Carona, self).save(
            force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
