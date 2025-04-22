###
# 03 - range()
# Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###

from os import system
if system("clear") != 0: system("cls")

print("range()")

nums = range(5) # no es [1,2,3,4,5]
print(type(nums))

print(nums) # range(0,5)

print('Range 1')

# Genera una secuencia de 0 a 9
for num in range(10):
  print(num)

print('Range 2')

for num in range(4,12):
  print(num)

print('Range 3 - step 2')
for num in range(0,10,2):
  print(num)

print('Range 3 - step negativo')
for num in range(10,0,-2):
  print(num)


print('Crea lista con range')
print(list(range(10)))

for _ in range(5):
  print('For sin crear variable')