def healing_potion() -> str:
    from .elements import create_fire
    from .elements import create_water
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    from .elements import create_fire, create_earth
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    from .elements import create_air as air, create_water as water
    return f"Invisibility potion brewed with {air()} and {water()}"


def wisdom_potion() -> str:
    import alchemy.elements
    fire = alchemy.elements.create_fire()
    air = alchemy.elements.create_air()
    water = alchemy.elements.create_water()
    earth = alchemy.elements.create_earth()
    string = "Wisdom potion brewed with all elements:"
    return f"{string}[{fire},{air},{water},{earth}]"
