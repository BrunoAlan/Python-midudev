
from os import system
if system("clear") != 0: system("cls")

print('For loop')

frutas = ['manzana', 'banana', 'naranja']

#iterar sobre una lista
for fruta in frutas:
    print(fruta)

#iterar sobre cualquier objeto iterable
cadena = "Alancito"
for caracter in cadena:
    print(caracter)

# Recuperar el indice de cada elemento = enumerate()

for index,fruta in enumerate(frutas):
    print(f"El indice de {fruta} es {index}")

# bucles anidados
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# break

animales = ['perro', 'gato', 'loro', 'pez']

for animal in animales:
    print(animal)
    if animal == 'loro':
        break

# continue
# con continue se salta la iteracion actual y continua con la siguiente

for animal in animales:
    if animal == 'loro':
        continue
    print(animal)

# comprension de listas - list comprehension

# For loop en una sola linea

animales = ['perro', 'gato', 'loro', 'pez', 'raton']

animales_mayusculaas = [animal.upper() for animal in animales]

print(animales_mayusculaas)

# Muestra los numeros pares de una lista

pares = [numero for numero in [1,2,3,4,5,6,7,8,9] if numero % 2 == 0]
print(pares)