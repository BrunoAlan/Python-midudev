###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

index = 1
while index <=10:
  print(index)
  index+=1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
index = 1
suma=0

while index <=20:
  suma+=index
  index+=1
else:
  print(suma)


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

number = int(input("Ingresa el nro que quieres el factorial"))
factorial=1
contador=1
while contador <= number:
  factorial *=contador
  print(factorial)
  contador+=1

print(f"Factorial de {number}: {factorial}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
isValid=False
while not isValid:
  password = input("Insert a password")
  if(len(password)>=8):
    isValid=True
    print('Contraseña válida')

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
number = int(input("Ingrese un numero para saber sus multiplos"))
counter=1

while counter<=10:
  print(counter * number)
  counter+=1


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

print("\nEjercicio 6:")
number = int(input("Ingrese un numero para saber sus primos"))
primos = []

# Verificamos los números desde 2 hasta number
current_num = 2
while current_num <= number:
    # Asumimos que el número es primo hasta que se demuestre lo contrario
    es_primo = True
    
    # Comprobar si current_num es divisible por algún número desde 2 hasta current_num-1
    divisor = 2
    while divisor * divisor <= current_num:  # Optimización: solo necesitamos verificar hasta la raíz cuadrada
        if current_num % divisor == 0:
            es_primo = False
            break
        divisor += 1
    
    # Si es primo, lo añadimos a la lista
    if es_primo:
        primos.append(current_num)
    
    current_num += 1

print(f"Los números primos hasta {number} son: {primos}")



