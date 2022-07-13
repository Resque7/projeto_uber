from django.http import HttpResponseRedirect #MENSAGEM PARA RESPONDER SE O FORMS FOI PREENCHIDO
from django.shortcuts import render
from django.urls import reverse

from .forms import NameUsuario
from .models import Usuario


from rest_framework import viewsets
from usuarios.serializers import UsuarioSerializer


def get_name(request):
    if request.method == 'POST':
        form = NameUsuario(request.POST)
        if form.is_valid():
            r = request.POST
            usuario = Usuario.objects.create(nome=r.get("nome"))
            return HttpResponseRedirect(reverse("inicio"))

    else:
        form = NameUsuario()

    return render(request, 'nome.html', {'form': form})


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API ENDPOINT THAT ALLOWS USERS TO VE VIEWED OR EDITED.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

