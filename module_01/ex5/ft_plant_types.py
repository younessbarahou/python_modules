#!/usr/bin/python3
""" A blueprint for creating plants instances """


class Plant:
    """ Constructor that initialize instance attributes """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


"""Flower instance inherits from Plant"""


class Flower(Plant):
    """ Constructor that initialize instance attributes """
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    """ Blooming """
    def bloom(self):
        return (f"{self.name} is blooming beautifully!\n")


"""Tree instance inherits from Plant"""


class Tree(Plant):
    """ Constructor that initialize instance attributes """
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    """ calculates the shade """
    def produce_shade(self):
        canopy = 20 * self.trunk_diameter // 100
        result = 3 * (canopy ** 2) // 4
        return (f"{self.name} provides {result} square meters of shade")


"""Vegetable instance inherits from Plant"""


class Vegetable(Plant):
    """ Constructor that initialize instance attributes """
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    flower_1 = Flower("Rose", 25, 30, "red")
    flower_2 = Flower("Jasmin", 30, 25, "orange")
    tree_1 = Tree("Oak", 500, 1825, 50)
    tree_2 = Tree("Palm", 800, 20, 20)
    vegetable_1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    vegetable_2 = Vegetable("Carrot", 180, 190, "winter", "vitamin D")
