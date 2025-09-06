from skat import *
from deck import *
from player import *

# initializing everything
deck = Deck()
game_rules = Skat()
hand1, hand2, hand3, skat = game_rules.deal_cards()

name1 = input("What is your name? ")
player1 = Player(name1, hand1)

name2 = input("What is your name? ")
player2 = Player(name2, hand2)

name3 = input("What is your name? ")
player3 = Player(name3, hand3)

player_order = [(player1, hand1), (player2, hand2), (player3, hand3)]

i : int = 0

last_round = False

while i < 10:
    if i == 9:
        last_round = True

    player_order = game_rules.play_round(player_order, last_round)
    i += 1

game_rules.calculate_winner(player1, player2, player3)

