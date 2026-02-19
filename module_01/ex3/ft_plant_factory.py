#!/usr/bin/python3
""" A blueprint for creating plants instances """


class Plant:
    """ Constructor that initialize instance attributes """
    def __init__(self, name, height, agee):
        self.name = name
        self.height = height
        self.agee = agee

    def get_info(self):
        return (f"Created: {self.name} ({self.height}cm, {self.agee} days)")


if (__name__ == "__main__"):
    print("=== Plant Factory Output ===")
    data_1 = {"p": "Rose", "height": 25, "age": 30}
    data_2 = {"p": "Cactus", "height": 10, "age": 99}
    data_3 = {"p": "Ractus", "height": 100, "age": 9}
    data_4 = {"p": "fern", "height": 75, "age": 2}
    data_5 = {"p": "oak", "height": 60, "age": 89}
    data_1 = Plant(data_1["p"], data_1["height"], data_1["age"])
    print(data_1.get_info())
    data_2 = Plant(data_2["p"], data_2["height"], data_2["age"])
    print(data_2.get_info())
    data_3 = Plant(data_3["p"], data_3["height"], data_3["age"])
    print(data_3.get_info())
    data_4 = Plant(data_4["p"], data_4["height"], data_4["age"])
    print(data_4.get_info())
    data_5 = Plant(data_5["p"], data_5["height"], data_5["age"])
    print(data_5.get_info())
    print("\nTotal plants created: 5")
