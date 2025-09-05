from deck import *

Hand : List[Card]

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.cards = []