##
# 01 - Expresiones regulares
#

from os import system

if system("clear") != 0:
    system("cls")
"""Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc."""


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""

# 1. importamos el modulo de expresiones regulares "re"
import re

# 2. crear el patron que es la cadena de text a encontrar
pattern = "Hola"

# 3. El texto donde queremos buscar
text = "Hola mundo"

# 4. Usamos la funcion re
result = re.search(pattern, text)

if result:
    print("Encotrado")
else:
    print("No encontrado")

# .group() -> Devuelve la cadena que coincide con el pattern
print(result.group())

# .start() -> devuelva la posición inicial de la coincidencia
print(result.start())

# .end() -> devuelva la posición final de la coincidencia
print(result.end())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"

found_ia = re.search(pattern, text)
if found_ia:
    print(f"IA empieza en {found_ia.start()} y termina en {found_ia.end()}")
else:
    print("No encontrado")


### Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.findall(pattern, text)
print(len(matches))


# iter() devuelve un iterador que contiene todos los resultados de la búsqueda

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())


# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"

pattern = "midu"

matches = re.finditer(pattern, text)

for match in matches:
    print(f"{match.group()} {match.start()}-{match.end()}")


# Modificadores

# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no está mala. Viva la Ia"
pattern = "IA"

found_ia = re.findall(pattern, text, re.IGNORECASE)
print(found_ia)

# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = "python"

found_python = re.findall(pattern, text, re.IGNORECASE)
print(found_python)

# Reemplazar texto .sub()

text = "Hola mundo, hola de nuevo!"
pattern = "Hola"
replacement = "adios"

new_text = re.sub(pattern, replacement, text, re.IGNORECASE)

print(new_text)
