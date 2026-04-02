from ex2.EliteCard import EliteCard, Spell
from ex0.Card import Rarity


if __name__ == "__main__":
    try:
        print("\n=== DataDeck Ability System ===\n")
        print("Playing Arcane Warrior (Elite Card):")
        print()
        print("- Card: ['play', 'get_card_info', 'is_playable']")
        print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
        print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
        print()
        print("Combat phase:")
        elite_1 = EliteCard(
            'Arcane Warrior', 5, Rarity.LEGENDARY, 5, 3, 5, 'melee', Spell.HEAL
        )
        elite_2 = EliteCard(
            'Enemy', 5, Rarity.COMMON, 3, 2, 5, 'melee', 'Waterball'
        )
        print(f"Attack result: {elite_1.attack(elite_2)}")
        print(f"Defense result: {elite_1.defend(5)}")
        print()
        print("Magic phase:")
        print(f"Spell cast: {elite_1.cast_spell('Ultimate', [elite_2])}")
        mana = 4
        print(f"Mana channel: {elite_1.channel_mana(mana)}")
        print()
        print("Multiple inteface implementation successful")
    except Exception as e:
        print(e)
