from skat import *
from deck import *
from player import *

# initializing everything
deck = Deck()
playing_rules = Skat()
hand1, hand2, hand3, skat = playing_rules.deal_cards()

name1 = input("What is your name? ")
player1 = Player(name1, hand1)

name2 = input("What is your name? ")
player2 = Player(name2, hand2)

name3 = input("What is your name? ")
player3 = Player(name3, hand3)

player_order = [(player1, hand1), (player2, hand2), (player3, hand3)]

i : int = 0

while i < 10:
    playing_rules.play_round(player_order)
    i += 1

