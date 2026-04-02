from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


if __name__ == "__main__":
    try:
        print()
        print("=== DataDeck Card Foundation ===")
        print()
        print("Testing Abstract Base Class Design:")
        print()
        card_1 = CreatureCard('Fire Dragon', 5, Rarity.LEGENDARY.value, 7, 5)
        print("CreatureCard Info:")
        print(card_1.get_card_info())
        print()
        print("Playing Fire Dragon with 6 mana available:")
        print(f"Playable: {card_1.is_playable(6)}")
        game_state = {
            'mana': 6,
            'effect': 'Creature Summoned',
            'players': ['player_1']
            }
        print(f"Play result: {card_1.play(game_state)}")
        print()
        print("Fire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {card_1.attack_target('Goblin Warrior')}")
        print()
        print("Testing insufficient mana (3 available):")
        print(f"Playable: {card_1.is_playable(3)}")
        print()
        print("Testing Error Case:")
        card_2 = CreatureCard('Water Dragon', 5, Rarity.COMMON.value, -5, -5)
        print("Abstract pattern successfully demonstrated!")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
