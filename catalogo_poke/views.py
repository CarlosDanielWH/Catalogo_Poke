import requests
from django.http import HttpResponse
from django.shortcuts import render


def catalogo(request):

    offset = request.GET.get('offset', 0)

    peticion = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=10&offset={}'.format(offset))

    datos = peticion.json()

    resultados = datos['results']

    for pokemon in resultados:

        url = pokemon['url']

        partes = url.split('/')

        pokemon_id = partes[-2]

        pokemon['id'] = pokemon_id

    return render(request, 'pokemon/catalogo.html', {
        'resultados':resultados,
        'offset': int(offset),
    })


