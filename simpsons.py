import requests
import random

url="https://thesimpsonsquoteapi.glitch.me/quotes"
mensaje=requests.get(url).json()
infoGeneral=mensaje[0]
cont=0
pista=[]
personaje=infoGeneral["character"]
ps=list(personaje)
for i in range(len(personaje)):
    pista.append("_")

print(f"Que personaje de los simpsons dijo: {infoGeneral["quote"]}")
print()

while cont!=3:
    ran=random.randint(0,len(personaje)-1)
    respuesta=input("Quien dijo esa frase? (se cuentan los .) ")
    for letra in personaje[ran]:
        pista[ran] = personaje[ran]
        print(personaje)
        if respuesta!=personaje.lower():
            print("la pista del nombre es:",pista)
            cont+=1
        else:
            print(f"Correcto el personaje es {personaje}")
            cont=3