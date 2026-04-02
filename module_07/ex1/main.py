from ex1.SpellCard import SpellCard, Effect
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.Deck import Deck


if __name__ == "__main__":
    try:
        print()
        print("=== DataDeck Deck Builder ===")
        print()
        print("Building deck with different card types...")
        deck = Deck()
        creature_card = CreatureCard(
            'Fire Dragon', 5, Rarity.LEGENDARY.value, 5, 5
            )
        spell_card = SpellCard(
            'Lightning Bolt', 3, Rarity.COMMON.value, Effect.HEAL.value
            )
        artifact_card = ArtifactCard(
            'Mana Crystal', 2, Rarity.RARE.value, 2, '+1 mana per turn'
            )
        deck.add_card(spell_card)
        deck.add_card(creature_card)
        deck.add_card(artifact_card)
        deck.shuffle()
        print(f"Deck stats: {deck.get_deck_stats()}")
        print("\nDrawing and playing cards:\n")
        game_state = {'mana': 10, 'targets': [], 'game_mode': 'Survival'}
        draw_1 = deck.draw_card()
        print(f"Drew: {draw_1.name} ({type(draw_1).__name__})")
        print(f"Play result: {draw_1.play(game_state)}")
        print()
        draw_2 = deck.draw_card()
        print(f"Drew: {draw_2.name} ({type(draw_2).__name__})")
        print(f"Play result: {draw_2.play(game_state)}")
        print()
        draw_3 = deck.draw_card()
        print(f"Drew: {draw_3.name} ({type(draw_3).__name__})")
        print(f"Play result: {draw_3.play(game_state)}")
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print()
        print(
            "Polymorphism in action: Same Inteface, different card behaviors"
            )
