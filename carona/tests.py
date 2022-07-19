
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

import django
django.setup()

from django.test import TestCase

from carona.models import Carona


class CaronaTest(TestCase):
    def test_pedircarona(self):
        carona = Carona(
            cliente='Dory',
            client_adress='P Sherman 42 Wallaby Way Sydney ',
            final_adress='Paredão',
            distancia=1000,
            carro_id=4
        )
        carona.save()

        self.assertEqual(carona.valor, 1000*0.57)
