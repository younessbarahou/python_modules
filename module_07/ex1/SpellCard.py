from ex0.Card import Card, Type
from typing import List
from enum import Enum


class Effect(Enum):
    DAMAGE = 'damage'
    HEAL = 'heal'
    BUFF = 'buff'
    DEBUFF = 'debuff'


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.playable = True
        self.type = Type.SPELL.value
        if self.effect_type == Effect.DAMAGE.value:
            self.description = 'Deal 1 damage to target'
        elif self.effect_type == Effect.HEAL.value:
            self.description = 'Heal +1 to target'
        elif self.effect_type == Effect.BUFF.value:
            self.description = 'Attack Increased +1'
        elif self.effect_type == Effect.DEBUFF.value:
            self.description = 'Attack Decreased -1'
        else:
            raise ValueError("Effect is not recognized !")

    def resolve_effect(self, targets: List[Card]) -> dict:
        for target in targets:
            if self.effect_type == Effect.DAMAGE.value:
                target.health -= 1
            elif self.effect_type == Effect.HEAL.value:
                target.health += 1
            elif self.effect_type == Effect.BUFF.value:
                target.attack += 1
            elif self.effect_type == Effect.DEBUFF.value:
                target.attack -= 1
        return {'status': 'effect applied successfully', 'cards': targets}

    def play(self, game_state: dict) -> dict:
        if self.playable is False:
            raise ValueError("Spell Already Used!")
        if game_state['mana'] < self.cost:
            raise ValueError("No Enough Mana To play!")
        game_state['mana'] -= self.cost
        self.resolve_effect(game_state['targets'])
        self.playable = False
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.description
            }
