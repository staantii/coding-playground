from deck import *

Hand : List[Card]

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.cards = []

    def get_all_cards(self, cards_from_round):
        self.cards.append(cards_from_round[0][1])
        self.cards.append(cards_from_round[1][1])
        self.cards.append(cards_from_round[2][1])
        print()
        print(self.cards)