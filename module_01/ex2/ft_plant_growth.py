#!/usr/bin/python3
""" A blueprint for creating plants instances """


class Plant:
    """ Constructor that initialize instance attributes """
    def __init__(self, name, height, agee):
        self.name = name
        self.height = height
        self.agee = agee

    """ instance method to increment age , self is the instance itself """
    def age(self):
        self.agee = self.agee + 1

    """ instance method to increment height """
    def grow(self):
        self.height = self.height + 1

    """ instance method to get plant informations """
    def get_info(self):
        return (f"{plant_1.name}: {plant_1.height}cm, {plant_1.agee} days old")


if (__name__ == "__main__"):
    cte = 0
    print("=== Day 1 ===")
    plant_1 = Plant("Rose", 25, 30)
    print(plant_1.get_info())
    while cte < 6:
        plant_1.age()
        plant_1.grow()
        cte = cte + 1
    print("=== Day 7 ===")
    print(plant_1.get_info())
    print(f"Growth this week: +{cte}cm")
