
from django import forms
from veiculos.models import Veiculo


class CadastroVeiculo(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa','modelo', 'cor', 'marca', 'ativo', 'proprietario']

    # name = forms.CharField(label='Nome Completo', max_length=100)