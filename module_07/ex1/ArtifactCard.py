from ex0.Card import Card, Type


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = Type.ARTIFACT.value

    def activate_ability(self) -> dict:
        if self.durability == 0:
            raise ValueError("Durability is 0 !")
        self.durability -= 1
        return {'effect': self.effect, 'durability': self.durability}

    def play(self, game_state: dict) -> dict:
        if game_state['mana'] < self.cost:
            raise ValueError("No Enough Mana to Play!")
        game_state['mana'] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
            }
