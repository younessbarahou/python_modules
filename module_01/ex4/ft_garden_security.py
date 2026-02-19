#!/usr/bin/python3
""" A blueprint for securing  """


class SecurePlant():
    """ Constructor that initialize instance attributes """
    def __init__(self, name, height, agee):
        self.__name = name
        self.__height = height
        self.__age = agee
        print(f"Plant Created: {self.__name}")

    """Getter => method to access encapsulated attributes (name,height,age)"""
    def get_name(self):
        return (self.__name)

    def get_height(self):
        return (self.__height)

    def get_age(self):
        return (self.__age)

    """Setter => method to Modify encapsulated attributes (height,age)"""
    def set_height(self, new_height):
        if new_height < 0:
            return (f"Operation [REJECTED]: height {new_height}cm is negative")

        self.__height = new_height
        return (f"Height updated: {new_height}cm [OK]")

    def set_age(self, new_age):
        if new_age < 0:
            return (f"Operation [REJECTED]: height {new_age}cm is negative")
        self.__age = new_age
        return (f"Age updated: {new_age} days [OK]")


if (__name__) == "__main__":
    print("=== Garden Security System ===")
    p = SecurePlant("Rose", 0, 0)
    print(p.set_height(25))
    print(p.set_age(30))
    print()
    print(p.set_age(-5))
    print(f"Current plant:{p.get_name()},{p.get_height()}cm,{p.get_age()}days")
