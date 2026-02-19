#!/usr/bin/python3
""" A blueprint for creating plants instances """


class Plant:
    """ Constructor that initialize instance attributes """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if (__name__ == "__main__"):
    print("=== Garden Plant Registry ===")
    plant_1 = Plant("Rose", 25, 30)
    plant_2 = Plant("Sunflower", 80, 45)
    plant_3 = Plant("Cactus", 15, 120)
    print(f"{plant_1.name}: {plant_1.height}cm, {plant_1.age} days old")
    print(f"{plant_2.name}: {plant_2.height}cm, {plant_2.age} days old")
    print(f"{plant_3.name}: {plant_3.height}cm, {plant_3.age} days old")
