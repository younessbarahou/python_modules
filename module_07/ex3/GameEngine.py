from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = []
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def simulate_turn(self) -> dict:
        self.hand = self.factory.create_themed_deck(4)
        battle_field = self.factory.create_themed_deck(2)
        result = self.strategy.execute_turn(self.hand, battle_field)
        self.cards_created += len(result['cards_played'])
        self.total_damage = result['damage_dealt']
        self.turns_simulated += 1
        return result

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': type(self.strategy).__name__,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
