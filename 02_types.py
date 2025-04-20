# Types in Python

# Python has several built-in types. The most common ones are:
# - int: Integer numbers
# - float: Floating point numbers
# - str: Strings
# - bool: Boolean values (True or False)
# - list: List of values
# - tuple: Immutable list of values
# - dict: Dictionary of key-value pairs
# - set: Unordered collection of unique values
# - None: Represents the absence of a value
# - complex: Complex numbers
# - bytes: Immutable sequence of bytes
# - bytearray: Mutable sequence of bytes
# - memoryview: Memory view object
# - range: Represents a range of numbers
# - frozenset: Immutable set

print("int")

print(10)
print(0)
print(-10)

print(type(10))

"""
 Asi es una cadena de texto
 multilinea, y si no se almacena en una variable
 se usa para comentar
"""

print("float")
print(10.0)
print(0.0)
print(type(1e0))

print("Complex")
print(10 + 5j)
print(0 + 0j)
print(type(10 + 5j))

print("str")
print("Hello World")
print("123")
print("")

print("bool")
print(True)
print(False)
print(type(True))
print(type(False))
print(type(1 == 1))
print(type(1 == 0))
print(type(1 != 0))
print(type(1 != 1))
print(type(1 > 0))
print(type(1 < 0))
print(type(1 >= 0))
print(type(1 <= 0))
print(type(1 > 0 and 1 < 0))
print(type(1 > 0 or 1 < 0))

print("NoneType")
print(None)
print(type(None))
