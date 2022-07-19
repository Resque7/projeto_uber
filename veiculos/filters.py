
import django_filters
from veiculos.const import COLORS
from veiculos.models import Veiculo, Marca


class VeiculoFilter(django_filters.FilterSet):
    cor = django_filters.ChoiceFilter(choices=COLORS)

    class Meta:
        model = Veiculo
        fields = {
            'modelo': ['icontains'],
        }


class MarcaFilter(django_filters.FilterSet):

    class Meta:
        model = Marca
        fields = {
            'nome': ['icontains'],
        }
