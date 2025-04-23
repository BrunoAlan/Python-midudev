###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

from os import system

if system("clear") != 0:
    system("cls")

# Ejemplo del diccionario

persona = {
    "nombre": "Alan",
    "age": 34,
    "sex": "male",
    "qualifications": [10, 9, 7],
    "is_student": True,
}


# Acceder a los valores

print(persona["nombre"])
print(persona["qualifications"][2])

persona["qualifications"][2] = 10
print(persona["qualifications"][2])

print(persona)

# eliminar completamente una propiedad

del persona["age"]
print(persona)

is_student = persona.pop("is_student")  # accedo a la key y la elimino
print(persona)


# Sobreescribir un diccionario con otro

a = {"name": "Alan", "age": 25}
b = {"name": "asd", "is_student": True}

a.update(b)

print(a)  # {'name': 'asd', 'age': 25, 'is_student': True}

# comprobar si existe una propiedad

print("name" in a)  # True

# obtener todas las claves
print(persona.keys())  # dict_keys(['nombre', 'sex', 'qualifications'])

# obtener todos los valores
print(persona.values())  # dict_values(['Alan', 'male', [10, 9, 10]])

# obtener clave valor
print(
    persona.items()
)  # dict_items([('nombre', 'Alan'), ('sex', 'male'), ('qualifications', [10, 9, 10])])


for key, value in persona.items():
    print(f"{key}:{value}")
