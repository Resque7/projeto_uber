
from .models import Carona

from rest_framework import viewsets
from carona.serializers import CaronaSerializer


class CaronaViewSet(viewsets.ModelViewSet):
    queryset = Carona.objects.all()
    serializer_class = CaronaSerializer
