from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from ex0.Card import Card
from typing import Dict, Any


class TournamentCard(Combatable, Rankable, Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        power: int,
        defense: int,
        health: int
    ) -> None:
        super().__init__(name, cost, rarity, power, defense, health)
        self.rating = self.calculate_rating()
        self.wins = 0
        self.losses = 0
        self.turn_history = {}

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self.cost:
            raise ValueError("No enough Mana To play!")
        game_state['mana'] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost
        }

    def attack(self, target: Card) -> dict:
        target.health -= self.power
        if target.health < 0:
            target.health = 0
        return {'attacker': self.name,
                'target': target.name,
                'damage': self.power
                }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        damage_blocked = self.defense - incoming_damage
        if damage_blocked == 0:
            damage_taken = 0
        elif damage_blocked > 0:
            damage_taken = 0
        elif damage_blocked < 0:
            damage_blocked = self.defense
            damage_taken = incoming_damage - self.defense
        self.defense -= damage_blocked
        self.health -= damage_taken
        return {'defender': self.name,
                'damage_taken': damage_taken,
                'damage_blocked': damage_blocked,
                'still_alive': True if self.health > 0 else False
                }

    def calculate_rating(self) -> int:
        self.rating = self.power * 100 + self.defense * 100
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_combat_stats(self) -> dict:
        return {
            'Attack': self.power,
            'Defense': self.defense,
            'Health': self.health
        }

    def get_tournament_stats(self) -> dict:
        return self.turn_history

    def get_rank_info(self) -> dict:
        record = f"{self.wins}-{self.losses}"
        return {
            'Rating': self.rating,
            'Record': record
        }
