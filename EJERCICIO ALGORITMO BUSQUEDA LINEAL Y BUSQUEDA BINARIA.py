import requests
response = requests.get("https://randomuser.me/api/?results=10")
data = response.json()

usuarios_filtrados = []

for usuario in data["results"]:
  nuevo_usuario = {
    "nombre": f"{usuario["name"]["first"]} {usuario["name"]["last"]}",
  }
  usuarios_filtrados.append(nuevo_usuario)

# print(usuarios_filtrados)


#busqueda lineal 
def busqueda_lineal(lista, objetivo):
  for i in range(len(lista)):
    if lista[i]["nombre"] == objetivo:
      return i
  return -1 

#aplicamos busqueda lineal
posicion_buscada = busqueda_lineal(usuarios_filtrados, "Carlos")



#---------------------------------------------------------------------------
import random 
#creamos una lista desordenada
numeros = list(range(1,101))
random.shuffle(numeros)


#la ordenamos
def ordenar_lista(lista):
  for i in range(len(lista)): 
    min = i
    for j in range(i + 1, len(lista)):
      if lista[j] < lista[min]:
        min = j
    lista[i], lista[min] = lista[min], lista[i]
  return lista

lista_ordenada = ordenar_lista(numeros)


#busqueda binaria
def busqueda_binaria(lista, objetivo):
  izquierda, derecha = 0, len(lista)-1
  while izquierda <= derecha:
    medio = (izquierda + derecha) // 2
    if lista[medio] == objetivo: 
      return medio
    elif lista[medio] < objetivo:
      izquierda = medio + 1
    else:
      derecha = medio - 1
  return -1


#aplicamos busqueda binaria
#buscamos el numero 84
posicion_Encontrada = busqueda_binaria(lista_ordenada, 84)
#busqueda con indice
resultado = lista_ordenada[83]
print(resultado)

