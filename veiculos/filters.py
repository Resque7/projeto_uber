
import django_filters
from veiculos.const import COLORS
from veiculos.models import Veiculo


class VeiculoFilter(django_filters.FilterSet):
    modelo = django_filters.CharFilter(field_name='modelo', lookup_expr='icontains')
    cor = django_filters.ChoiceFilter(choices=COLORS)
    marca = django_filters.CharFilter(field_name='marca', lookup_expr='icontains')

    class Meta:
        model = Veiculo
        fields = ['modelo', 'cor', 'marca']



