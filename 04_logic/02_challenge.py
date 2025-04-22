"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

from os import system
if system("clear") != 0: system("cls")

def check_eggs(eggs:list)->int:
  sum=0
  for egg in eggs:
    if(egg %2==0):
      sum+=egg
  return sum

print(check_eggs([2,3,4,5,6]))