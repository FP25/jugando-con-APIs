import random as ran
from tkinter.tix import IMAGE

import requests
import PIL
from PIL.Image import Image


def estado(valor):
    if valor.lower()=="alive":
        return print("El personaje esta vivo.")
    elif valor.lower()=="unknown":
        return print("el estado del personaje es desconocido.")
    else:
        return print("El personaje esta muerto.")
def especieYtipo(valor,tipo):
    if valor.lower() == "humanoid":
        return print("El personaje es un humanoide. Y es de tipo,",tipo)
    elif valor.lower() == "human":
        return print("El personaje es un humano. Y es de tipo,",tipo)
    elif valor.lower() == "animal":
        return print("El personaje es un animal. Y es de tipo,",tipo)
    elif valor.lower() == "alien":
        return print("El personaje es un alien. Y es de tipo,",tipo)
    elif valor.lower() == "robot":
        return print("El personaje es un robot. y es de tipo,",tipo)
    elif valor.lower() == "cronenberg":
        return print("El personaje es un cronenberg. Y es de tipo,",tipo)
    elif valor.lower() == "disease":
        return print("El personaje es un disease. Y es de tipo,",tipo)
    elif valor.lower() == "mythological creature":
        return print("El personaje es una criatura mitologica. Y es de tipo,",tipo)
    elif valor.lower() == "unknown":
        return print("Se desconoce la especie del personaje. Y es de tipo,",tipo)
def genero(valor):
    if valor.lower() == "male":
        return print("El personaje es hombre.")
    elif valor.lower() == "unknown":
        return print("Se desconoce el genero del personaje.")
    elif valor.lower() == "female":
        return print("El personaje es mujer.")
    elif valor.lower() == "genderless":
        return print("El personaje no tiene genero.")
def preguntaAleatoria(num,valores):
    if num == 1:
        estado(valores[2])
    elif num == 2:
        especieYtipo(valores[3],valores[4])
    elif num == 3:
        genero(valores[5])
    elif num == 4:
        print("El personaje es originario de:",valores[6]["name"])
    elif num == 5:
        print("El personaje se encuentra en:",valores[7]["name"])


url= "https://rickandmortyapi.com/api/character/"
num=ran.randint(1,826)
personaje=requests.get(f"{url}{num}").json()
respuesta=""
cont=0
valores=list(personaje.values())
while cont!=3 and respuesta!=valores[1].lower():
    pregunta=ran.randint(1,5)
    preguntaAleatoria(2,valores)
    respuesta=input("Que personaje es: ")
    cont+=1
print()
print(f"El personaje es: {valores[1]}")
