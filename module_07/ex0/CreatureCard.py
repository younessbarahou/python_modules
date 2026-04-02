from ex0.Card import Card, Type
from typing import Dict, Any


class CreatureCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int
    ) -> None:
        if attack <= 0 or health <= 0:
            raise ValueError(
                "=> Card's attack and health should be positive!"
                )
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = Type.CREATURE.value
        self.effect = 'Creature summoned to battlefield'

    def play(self, game_state: Dict[str, Any]) -> dict:
        if game_state['mana'] < self.cost:
            raise ValueError("No enough Mana To play!")
        game_state['mana'] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }

    def attack_target(self, target: str) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }

    def get_card_info(self) -> dict:
        result = super().get_card_info()
        result.update({
            'type': self.type,
            'attack': self.attack,
            'health': self.health
            })
        return result
