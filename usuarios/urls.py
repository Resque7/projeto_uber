
from django.urls import path
from rest_framework import routers

from usuarios.views import *

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='api_usuarios')


urlpatterns = [
    path('', get_name, name='usuarios'),
] + router.urls
