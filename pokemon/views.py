from django.shortcuts import render, redirect
import requests, time

# Create your views here.

def pokemon_info(request, id):

    inicio = time.time()

    peticion = requests.get('https://pokeapi.co/api/v2/pokemon/' + id + '/')

    fin = time.time()

    if peticion.status_code != 200:
        print("La lista esta vacia")
        return render(request, 'pokemon/info_error.html', {} )

    print('Tiempo PokeAPI:', fin - inicio)

    datos = peticion.json()

    imagen = datos['sprites']['other']['official-artwork']['front_default']
        
    return render(request, 'pokemon/info_poke.html', {'pokemon':datos, 'imagen': imagen})



def catalogo_tipos(request, tipo):

    peticion = requests.get('https://pokeapi.co/api/v2/type/' + tipo + '/')

    datos = peticion.json()

    resultados = datos['pokemon']

    for pokemon in resultados:

        url = pokemon['pokemon']['url']

        partes = url.split('/')

        pokemon_id = partes[-2]

        pokemon['id'] = pokemon_id

    return render(request, 'pokemon/catalogo_tipos.html', {
            'resultados':resultados,
        })
    