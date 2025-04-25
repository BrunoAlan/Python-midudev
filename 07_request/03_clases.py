# 1. Intro to classes on python

# Classes are a way to create objects in python

from os import system

if system("clear") != 0:
    system("cls")


class Car:
    type = "vehicle with 4 wheels"

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def start(self):
        print(f"{self.brand} {self.model} is starting")


myCar = Car("toyota", "corolla", "red")


myCar.start()
