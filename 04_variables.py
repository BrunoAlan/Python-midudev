
# Variables in Python

# Python es de tipado dinamico y de tipado fuerte
# Tipado dinamico
# En Python no es necesario declarar el tipo de variable
# Tipado fuerte
# En Python no se puede cambiar el tipo de una variable

#Asignacion
my_name = 'Alan'
print(my_name)

age = 34
print(age)
# Reasignacion
age = 35
print(age)

# Tipado dinamico, se determina el tipo de variable en tiempo de ejecucion

name:str = 'Alan'
print(type(name)) # <class 'str'>

# print f string7
print(f"{my_name} is {age - 3} years old")


# Asignacion multiple
name, age, is_student = 'Alan', 34, True

print(name, age, is_student)

# Convenciones de nombres de variables
# snake_case
mi_variable = 'Hola'

MI_CONSTANTE_PI = 3.14  # uppercase par constantes 
