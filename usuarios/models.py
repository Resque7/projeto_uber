from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=70, null=False, blank=False, verbose_name="Nome Completo")

    def __str__(self):
        return self.nome

