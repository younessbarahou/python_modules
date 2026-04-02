from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard
from ex0.Card import Rarity


if __name__ == "__main__":
    try:
        print("\n=== DataDeck Tournament Platform ===\n")
        print("Registering Tournament Cards...")
        print()
        tournament = TournamentPlatform()
        card_1 = TournamentCard(
            'Fire Dragon',
            2, Rarity.LEGENDARY.value, 9, 8, 5)
        card_2 = TournamentCard(
            'Ice Wizard', 2, Rarity.LEGENDARY.value, 10, 6, 5)
        card_1_id = tournament.register_card(card_1)
        card_2_id = tournament.register_card(card_2)
        for card in tournament.cards:
            rank_info = card.get_rank_info()
            print(f"{card.name} (ID: {card.id})")
            print(f"Rating: {rank_info['Rating']}")
            print(f"Record: {rank_info['Record']}")
            print()
        print("Creating tournament match...")
        match1 = tournament.create_match('Dragon_01', 'Wizard_02')
        print(match1)
        print()
        print("Tournament Leaderboard:")
        leaderboard = tournament.get_leaderboard()
        index = 1
        for card in leaderboard:
            info = card.get_rank_info()
            name = card.name
            print(
                f"{index}.{name} - Rating: {info['Rating']} {info['Record']}"
                )
        print()
        print("Platform Report:")
        report = tournament.generate_tournament_report()
        print(report)
        print()
        print("=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except Exception as e:
        print(e)
