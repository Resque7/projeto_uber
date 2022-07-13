
from carona.models import Carona
from rest_framework import serializers

from veiculos.serializers import VeiculoSerializer


class CaronaSerializer(serializers.ModelSerializer):
    carro = VeiculoSerializer(read_only=True)

    class Meta:
        model = Carona
        fields = ['cliente', 'client_adress', 'final_adress', 'distancia', 'carro', 'valor']
        read_only_fields = ('valor', 'carro')
#read-only fields
