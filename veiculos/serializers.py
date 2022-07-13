from usuarios.serializers import UsuarioSerializer
from veiculos.models import Veiculo, Marca
from rest_framework import serializers


class VeiculoSerializer(serializers.ModelSerializer):
    proprietario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Veiculo
        fields = ['placa', 'modelo', 'cor', 'marca', 'ativo', 'proprietario']


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

