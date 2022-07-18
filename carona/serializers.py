
from carona.models import Carona
from rest_framework import serializers

from veiculos.serializers import VeiculoSerializer


class CaronaSerializer(serializers.ModelSerializer):
    carro = VeiculoSerializer(read_only=True)

    class Meta:
        model = Carona
        fields = ['cliente', 'client_adress', 'final_adress', 'distancia', 'valor', 'carro']
        read_only_fields = ('valor', 'carro'),

    # def create(self, validated_data):
    #     try:
    #         self.carro = Carona.objects.get(id=validated_data.get('valor'))
    #     except Carona.DoesNotExist:
    #         raise Exception("O ID DO VEICULO INFORMADO NÃO EXISTE"),
    #         super(CaronaSerializer, self).create(validated_data),
