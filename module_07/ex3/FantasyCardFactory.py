from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, Effect
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Card, Rarity
from random import choice, randint
from typing import Union


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.supported_types = {
            'type_1': CreatureCard.__name__,
            'type_2': SpellCard.__name__,
            'type_3': ArtifactCard.__name__}

    def create_creature(
            self,
            name_or_power: Union[str, int, None] = None
    ) -> Card:
        samples = ['Dragons', 'Goblins', "Valkery"]
        if name_or_power is None:
            name_or_power = choice(samples)
        rarities = [r.value for r in Rarity]
        creature = CreatureCard(
            name_or_power,
            randint(1, 5),
            choice(rarities),
            randint(1, 5),
            randint(1, 5))
        return creature

    def create_spell(
        self, name_or_power: Union[str, int, None] = None
    ) -> Card:
        samples = ['Fire', 'Ice', "Lightning"]
        if name_or_power is None:
            name_or_power = choice(samples)
        rarities = [r.value for r in Rarity]
        effects = [e.value for e in Effect]
        spell = SpellCard(
            name_or_power, randint(1, 5), choice(rarities), choice(effects))
        return spell

    def create_artifact(
        self,
        name_or_power: Union[str, int, None] = None
    ) -> Card:
        samples = ['Rings', 'Staffs', "Crystals"]
        if name_or_power is None:
            name_or_power = choice(samples)
        rarities = [r.value for r in Rarity]
        artifact = ArtifactCard(
            name_or_power, randint(1, 5), choice(rarities),
            randint(1, 5), '+1 mana'
            )
        return artifact

    def create_themed_deck(self, size: int) -> dict:
        index = 0
        card_types = [
            self.create_creature,
            self.create_spell, self.create_artifact
        ]
        result = []
        while index < size:
            result.append(choice(card_types)())
            index += 1
        return result

    def get_supported_types(self) -> dict:
        return self.supported_types
