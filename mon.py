import requests
def llamaApiPoke():
    url="https://pokeapi.co/api/v2/pokemon-species?offset=0&limit=1025"
    try:
        responde=requests.get(url)
        if responde.status_code==200:
            llamada=responde.json()
            return llamada
        else:
            print("error")
    except:
        print("n")

obj=llamaApiPoke()
listapoke=obj["results"]
for pokemon in listapoke:
    if pokemon["name"]=="banette":
        print(pokemon)