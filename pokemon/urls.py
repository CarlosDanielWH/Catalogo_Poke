
from django.conf.urls import url
from .views import pokemon_info, catalogo_tipos

urlpatterns = [
    url(r'^pokemon/([0-9]+)/$', pokemon_info, name='pokemon_info'),
    url(r'^types/([a-z]+)/$', catalogo_tipos, name='types'),

]