from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from random import shuffle
from math import ceil


class Deck:
    def __init__(self):
        self.cards = []
        self.creatures = 0
        self.spells = 0
        self.artifacts = 0
        self.avg_cost = 0

    def add_card(self, card: Card) -> None:
        if isinstance(card, CreatureCard):
            self.creatures += 1
        elif isinstance(card, SpellCard):
            self.spells += 1
        elif isinstance(card, ArtifactCard):
            self.artifacts += 1
        else:
            raise TypeError("Invalid Card added !")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                if isinstance(card, CreatureCard):
                    self.creatures -= 1
                elif isinstance(card, SpellCard):
                    self.spells -= 1
                elif isinstance(card, ArtifactCard):
                    self.artifacts -= 1
                return (True)
        return (False)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) == 0:
            raise ValueError("No cards to draw !")
        current_draw = self.cards[0]
        self.remove_card(current_draw.name)
        return current_draw

    def get_deck_stats(self) -> dict:
        costs = [card.cost for card in self.cards]
        if len(costs) != 0:
            self.avg_cost = float(ceil(sum(costs) / len(costs)))
        else:
            self.avg_cost = 0
        total = self.artifacts + self.creatures + self.spells
        return {'total_cards': total,
                'creatures': self.creatures,
                'artifacts': self.artifacts,
                'spells': self.spells,
                'avg_cost': self.avg_cost}
