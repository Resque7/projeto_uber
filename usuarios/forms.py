
from django import forms

from usuarios.models import Usuario


class NameUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome']

    # name = forms.CharField(label='Nome Completo', max_length=100)
