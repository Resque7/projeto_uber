
from django.urls import path
from veiculos.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'veiculos', VeiculoViewSet, basename='api_veiculos')
router.register(r'marcas', MarcaViewSet, basename='api_marcas')


urlpatterns = [
    path('', form_veiculo, name='veiculos')
] + router.urls
