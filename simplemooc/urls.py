
from django.contrib import admin
from django.urls import path

from veiculos.views import hello_word


urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello_word/', hello_word)
]
