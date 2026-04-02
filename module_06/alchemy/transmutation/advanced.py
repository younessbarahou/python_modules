from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    healing = healing_potion()
    gold = lead_to_gold()
    return f"Philosophers's stone created using {gold} and {healing}"


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
