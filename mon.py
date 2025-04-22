import random
import requests

ran=random.randint(1,1025)
llamada=requests.get(f"https://pokeapi.co/api/v2/pokemon/{ran}/").json()

pokemon=llamada["forms"][0]["name"]
tipos=[]
for i in range(len(llamada["types"])):
    tipos.append(llamada["types"][i]["type"]["name"])

acierto = []
respuesta=""
seguir=True
mal=0
while seguir and mal!=2:
    respuesta=input(f"El pokemon {pokemon} de que tipo o tipos es? ")
    if respuesta in tipos:
        acierto.append(respuesta)
        print(f"{pokemon} tiene ese tipo")
    else:
        print(f"{pokemon} no tiene ese tipo")
        mal+=1
    if acierto==tipos:
        seguir=False

if seguir==False:
    print(f"Bien hecho, el pokemon: {pokemon} es de tipo {tipos}")
else:
    print(f"Buen intento, pero el pokemon {pokemon} en realidad es de tipo {tipos}")