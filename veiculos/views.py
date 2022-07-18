
from django.http import HttpResponseRedirect #MENSAGEM PARA RESPONDER SE O FORMS FOI PREENCHIDO
from django.shortcuts import render
from django.urls import reverse

from .forms import CadastroVeiculo
from .models import Veiculo, Marca

from rest_framework import viewsets
from veiculos.serializers import VeiculoSerializer, MarcaSerializer


def form_veiculo(request):
    if request.method == 'POST':
        form = CadastroVeiculo(request.POST)
        if form.is_valid():
            r = request.POST
            Veiculo.objects.create(
                placa=r.get("placa"),
                modelo=r.get("modelo"),
                cor=r.get("cor"),
                marca_id=r.get("marca"),
                ativo=r.get("ativo") == 'on',
                proprietario_id=r.get("proprietario"),
            )

            return HttpResponseRedirect(reverse("inicio"))

    else:
        form = CadastroVeiculo()

    return render(request, 'veiculo.html', {'form': form})


def cadatro_sucesso(request):
    return render(request, 'cadastro_sucesso.html')


class VeiculoViewSet(viewsets.ModelViewSet):
    """
    API ENDPOINT THAT ALLOWS USERS TO VE VIEWED OR EDITED.
    """
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
