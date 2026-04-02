from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card, Rarity
from enum import Enum
from typing import List


class Spell(Enum):
    DAMAGE = 'damage'
    HEAL = 'heal'


class EliteCard(Combatable, Magical, Card):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: Rarity,
                 power: int,
                 defense: int,
                 health: int,
                 combat_type: str,
                 spell_type: Spell):
        super().__init__(name, cost, rarity, power, defense, health)
        self.combat_type = combat_type
        self.spell_type = spell_type

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self.cost:
            raise ValueError("No enough Mana To play!")
        game_state['mana'] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
        }

    def attack(self, target: Card) -> dict:
        target.health -= self.power
        if target.health < 0:
            target.health = 0
        return {'attacker': self.name,
                'target': target.name,
                'damage': self.power,
                'combat_type': self.combat_type}

    def defend(self, incoming_damage: int) -> dict:
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

    def get_combat_stats(self) -> dict:
        return {
            'combat name': self.name,
            'attack': self.attack,
            'defense': self.defense}

    def cast_spell(self, spell_name: str, targets: List[Card]) -> dict:
        for target in targets:
            if spell_name == Spell.DAMAGE.value:
                target.health -= 1
            elif spell_name == Spell.HEAL.value:
                target.health += 1
        target_names = [t.name for t in targets]
        return {'caster': self.name,
                'spell': spell_name,
                'targets': target_names,
                'mana_used': self.cost}

    def channel_mana(self, amount: int) -> dict:
        amount += 3
        return {'channeled': 3, 'total_mana': amount}

    def get_magic_stats(self) -> dict:
        return {
            'spell_name': self.name,
            'spell type': self.spell_type
        }
