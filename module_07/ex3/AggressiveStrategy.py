from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard


class AggressiveStrategy(GameStrategy):
    def __init__(self) -> None:
        self.name = 'Aggressive'

    def prioritize_targets(self, available_targets: list) -> list:
        def get_cost(card: Card) -> int:
            return card.cost
        targets = [
            t for t in available_targets
            if type(t) is CreatureCard
        ]
        targets.sort(key=get_cost)
        return targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        available_mana = 5
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        targets_attacked = self.prioritize_targets(battlefield)
        hand = [
            h for h in hand
            if type(h) is CreatureCard
            or type(h) is SpellCard
        ]
        for card in hand:
            if card.cost > available_mana:
                continue
            cards_played.append(card)
            available_mana -= card.cost
            mana_used += card.cost
            damage_dealt += 2
        cards_played = [c.name for c in cards_played]
        targets_attacked = [t.name for t in targets_attacked]
        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return self.name
