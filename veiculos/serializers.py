from usuarios.serializers import UsuarioSerializer
from veiculos.models import Veiculo, Marca
from rest_framework import serializers


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['nome']


class VeiculoSerializer(serializers.ModelSerializer):
    proprietario = UsuarioSerializer(read_only=True)
    marca = MarcaSerializer(read_only=True)
    cor = serializers.SerializerMethodField("get_cor")

    def get_cor(self, object):
        return object.get_cor_display()

    class Meta:
        model = Veiculo
        fields = ['placa', 'modelo', 'cor', 'marca', 'ativo', 'proprietario']
        read_only_fields = ('cor', 'marca')

