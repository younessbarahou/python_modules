from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards = []
        self.platform_active = False
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = card.name.split(' ')[1]
        card_id += f'_0{len(self.cards) + 1}'
        card.id = card_id
        self.cards.append(card)
        self.platform_active = True
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = [card1 for card1 in self.cards if card1.id == card1_id]
        card2 = [card2 for card2 in self.cards if card2.id == card2_id]
        if len(card1) == 0:
            raise ValueError(
                "1Both Card Should Be registered before creating a match !"
                )
        if len(card2) == 0:
            raise ValueError(
                "2Both Card Should Be registered before creating a match !"
                )
        elif card1_id == card2_id:
            raise ValueError("Card cant Attack Itself !")
        card1 = card1[0]
        card2 = card2[0]
        card1.attack(card2)
        card2.attack(card1)
        self.matches_played += 1
        if card1.power > card2.power:
            card1.update_wins(1)
            card2.update_losses(1)
            card1.rating += 16
            card2.rating -= 16
            card1.turn_history.update({'enemy': card2.id, 'result': 'win'})
            card2.turn_history.update({'enemy': card1.id, 'result': 'lose'})
            return {
                'winner': card1.id,
                'loser': card2.id,
                'winner_rating': card2.rating,
                'looser_rating': card1.rating
            }
        elif card2.power > card1.power:
            card1.update_losses(1)
            card2.update_wins(1)
            card1.rating -= 16
            card2.rating += 16
            card1.turn_history.update({'enemy': card2.id, 'result': 'lose'})
            card2.turn_history.update({'enemy': card1.id, 'result': 'win'})
            return {
                'winner': card2.id,
                'loser': card1.id,
                'winner_rating': card2.rating,
                'looser_rating': card1.rating
            }
        card1.turn_history.update({'enemy': card2.id, 'result': 'draw'})
        card2.turn_history.update({'enemy': card1.id, 'result': 'draw'})
        return {'Draw': 'No winner/looser for this game'}

    def get_leaderboard(self) -> list:
        def get_rating(card: TournamentCard) -> None:
            return card.rating
        self.cards.sort(key=get_rating, reverse=True)
        return self.cards

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        matches_played = self.matches_played
        ratings = [card.rating for card in self.cards]
        avg_rating = sum(ratings) / len(ratings)
        return {
            'total_cards': total_cards,
            'matches_played': matches_played,
            'avg_rating': int(avg_rating),
            'platform_status': 'active' if self.platform_active else 'inactive'
        }
