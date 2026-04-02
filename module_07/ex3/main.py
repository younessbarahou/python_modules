from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


if __name__ == "__main__":
    try:
        print("\n=== DataDeck Game Engine ===\n")
        print("Configuring Fantasy Card Game...")
        engine = GameEngine()
        Fcard_factory = FantasyCardFactory()
        strategy = AggressiveStrategy()
        engine.configure_engine(Fcard_factory, strategy)
        print(f"Factory: {type(Fcard_factory).__name__}")
        print(f"Strategy: {type(strategy).__name__}")
        print(f"Available types: {engine.factory.get_supported_types()}")
        print()
        print("simulating aggressive turn...")
        turn = engine.simulate_turn()
        cards_in_hand = {card.name: card.cost for card in engine.hand}
        print(f"Hand: {cards_in_hand}")
        print()
        print("Turn execution: ")
        print(f"Strategy: {type(engine.strategy).__name__}")
        print(f"Actions: {turn}")
        print()
        print("Game Report: ")
        print(engine.get_engine_status())
        print()
        print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
    except Exception as e:
        print(e)
