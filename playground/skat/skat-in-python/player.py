from deck import *

Hand : List[Card]

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.cards = []

    def __str__(self):
        return f'Player {self.name}'

    def get_all_cards(self, cards_from_round):
        self.cards.append(cards_from_round[0][1])
        self.cards.append(cards_from_round[1][1])
        self.cards.append(cards_from_round[2][1])
        print()
        print(self.cards)

    def get_skat(self, skat):
        self.cards.extend(skat)

    def get_points(self):
        points = 0
        for card in self.cards:
            points += card[1]

        new_tuple = (self.name, points)
        return new_tuple
