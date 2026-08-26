
from django.conf.urls import url, include
from django.contrib import admin
from views import catalogo

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pokemon/', include('pokemon.urls', namespace='pokemon')),
    url(r'^$', catalogo, name='catalogo'),
]
