import random
from deck import *

init_deck = Deck()

class Skat:
    def __init__(self):
        self.hand1 = []
        self.hand2 = []
        self.hand3 = []
        self.skat = []

    def deal_cards(self):
        new_deck = init_deck.get_deck()
        random.shuffle(new_deck)
        for i in range(0,9):
            self.hand1.append(new_deck[i])
        for i in range(10,19):
            self.hand2.append(new_deck[i])
        for i in range(20, 29):
            self.hand3.append(new_deck[i])
        for i in range(30, 32):
            self.skat.append(new_deck[i])

        print(self.hand1)
        print(self.hand2)
        print(self.hand3)
        print(self.skat)





skat = Skat()
skat.deal_cards()