
from rest_framework.response import Response
from .models import Carona
from rest_framework import viewsets, status
from carona.serializers import CaronaSerializer


class CaronaViewSet(viewsets.ModelViewSet):
    queryset = Carona.objects.all()
    serializer_class = CaronaSerializer

    def create(self, request, *args, **kwargs):
        payload = request.data

        Carona.objects.create(
            cliente=payload.get('cliente'),
            client_adress=payload.get('client_adress'),
            final_adress=payload.get('final_adress'),
            carro_id=payload.get('carro'),
            distancia=payload.get('distancia')
        )

        serializer = self.get_serializer(data=payload)
        serializer.is_valid(raise_exception=False)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

