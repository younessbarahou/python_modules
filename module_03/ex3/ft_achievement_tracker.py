if __name__ == "__main__":
    alice = {
        'first_kill',
        'level_10',
        'treasure_hunter',
        'speed_demon'
    }
    bob = {
        'first_kill',
        'level_10',
        'boss_slayer',
        'collector'
    }
    charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
    }
    print("== Achievement Tracker System ===")
    print()
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()
    print("=== Achievement Analytics ===")
    unique = alice.union(bob, charlie)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")
    print()
    common = alice.intersection(bob, charlie)
    rare_1 = alice.difference(bob, charlie)
    rare_2 = bob.difference(alice, charlie)
    rare_3 = charlie.difference(alice, bob)
    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player) : {rare_1.union(rare_2, rare_3)}")
    print()
    a_b_common = alice.intersection(bob)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    print(f"Alice vs Bob common: {a_b_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")
