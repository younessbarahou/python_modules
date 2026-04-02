from abc import ABC, abstractmethod


class Combatable(ABC):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        power: int,
        defense: int,
        health: int
    ) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        if power <= 0 or health <= 0:
            raise ValueError("attack / health should be positive !")
        self.power = power
        self.defense = defense
        self.health = health

    @abstractmethod
    def attack(self, target) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
