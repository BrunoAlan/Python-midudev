
# Input es una función que permite leer datos por teclado

print("Enter your name: ")
name = input()
print("Hello, " + name + "!")



age = input("Enter your age: " )
print(f"in 5 years you will be {int(age) + 5} years old") 
# input devuelve un string, por lo que hay que convertirlo a int


print("Get more than one input")
counrty,city = input("Enter your country and city: \n").split()