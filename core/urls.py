
from django.contrib import admin
from django.urls import path, include

from veiculos.views import cadatro_sucesso

from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('veiculos/', include('veiculos.urls')),
    path('cadastro_sucesso/', cadatro_sucesso, name="inicio"),
    path('carona/', include('carona.urls')),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

