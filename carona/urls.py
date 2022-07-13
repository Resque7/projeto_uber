
from carona.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'carona', CaronaViewSet, basename='api_carona')

urlpatterns = [
] + router.urls
