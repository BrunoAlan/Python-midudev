###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

from os import system
if system("clear") != 0: system("cls")

# Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = []
lista_de_listas= [[1,2],[3,4]]
matrix = [[1,2],[2,3],[4,5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos de una lista por índice
print("\nAcceso a elementos de una lista por índice")
print(lista2[0]) #manzanas
print(lista2[1]) #peras
print(lista2[-1]) #plátanos -> último elemento


print(lista_de_listas[1][0]) #3

# Slicing
print("Slicing")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3]) # [1, 2, 3]
print(lista1[3:]) # [4, 5]

#hace una copia de la lista
print(lista1[:]) # [1, 2, 3, 4, 5]

# Más magia
print("Más magia")

# lista[desde:hasta:paso]
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista1[::2]) # [1, 3, 5, 7, 9]
print(lista1[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Modificar una lista
print("\nModificar una lista")
lista1 = [1, 2, 3, 4, 5]
lista1[0] = 10 # Cambia el primer elemento

# Añadir elementos a una lista
print("\nAñadir elementos a una lista")
lista1 = [1, 2, 3, 4, 5]

# forma larga y menos eficiente
lista1 = lista1 + [6,7,8]
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8]

# forma corta y más eficiente
lista1 += [9,10,11] 
print(lista1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# longitud de una lista
print("\nLongitud de una lista")
lista1 = [1, 2, 3, 4, 5]
print(len(lista1)) # 5

