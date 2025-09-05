import random
from symbol import continue_stmt

from deck import *
from player import *


#player_order : List[Tuple[Player, Hand]]

init_deck = Deck()

# Basic rule set and order of rounds
class Skat:
    def __init__(self):
        self.hand1 = []
        self.hand2 = []
        self.hand3 = []
        self.skat = []
        self.current_round_cards = []

    def deal_cards(self):
        # method to distribute cards among three hands and a skat
        new_deck = init_deck.get_deck()
        random.shuffle(new_deck)
        for i in range(0,10):
            self.hand1.append(new_deck[i])
        for i in range(10,20):
            self.hand2.append(new_deck[i])
        for i in range(20, 30):
            self.hand3.append(new_deck[i])
        for i in range(30, 32):
            self.skat.append(new_deck[i])

        return self.hand1, self.hand2, self.hand3, self.skat

    def play_round(self, player_order, last_round):
        # everybody makes their move and the first one declares a color
        color = self.player_move(player_order[0][0], player_order[0][1])
        self.player_move(player_order[1][0], player_order[1][1], color)
        self.player_move(player_order[2][0], player_order[2][1], color)

        # the moves get evaluated and a winner is determined
        winner = self.evaluate(self.current_round_cards, color)
        winner.get_all_cards(self.current_round_cards)
        self.current_round_cards.clear()

        # on the last round the winner gets the skat
        if last_round:
            winner.get_skat(self.skat)

        # the player order for the next round is determined
        #new_player_order = self.get_player_order(winner)
        #return new_player_order

    def get_player_order(self, winner):
        new_player_order = []


    def evaluate(self, who_played_what, color):
        # decides who gets all the cards
        first_move = who_played_what[0]
        second_move = who_played_what[1]
        third_move = who_played_what[2]
        trump_game = False

        if first_move[1][1] == 2:
            trump_game = True

        best_move = first_move

        if second_move[1][0] == color and second_move[1][1] > best_move[1][1]:
            best_move = second_move

        if third_move[1][0] == color and third_move[1][1] > best_move[1][1]:
            best_move = third_move

        print()
        print(str(best_move[0].name) + " gets all cards from this round! They played: (" + str(best_move[1][0].name) + ", " + str(best_move[1][1].name) + ").")

        return best_move[0]


    def player_move(self, player, hand, color = None):
        # simulates one move from one player

        # first of all we check if the player has a valid card to play or if the player is the first of it's round
        has_a_valid_card = False
        init_color = False

        if color is None:
            init_color = True
            pass
        else:
            for card in hand:
                if card[0] == color:
                    has_a_valid_card = True

        # now starting the move
        print(str(player.name) + "s turn! You have the following cards: ")
        self.print_hand(hand)

        while True:
            # player decides on a card and fets checked if it's a valid move
            index = input("Enter the number of the card you would like to play: ")
            index = int(index) - 1
            card_to_play = hand[index]
            print(card_to_play)
            if has_a_valid_card and card_to_play[0] == color:
                break
            elif init_color:
                color = card_to_play[0]
                break
            elif not has_a_valid_card and not init_color:
                break
            else:
                print("You have a valid card. Please play it.")

        hand.remove(card_to_play)

        new_tuple = (player, card_to_play)

        self.current_round_cards.append(new_tuple)
        return color

    def calculate_winner(self, player1, player2, player3):
        player1_points = player1.get_points()
        player2_points = player2.get_points()
        player3_points = player3.get_points()

        winner = player1_points

        if player2_points[1] < winner[1]:
            winner = player2_points

        if player3_points[1] < winner[1]:
            winner = player3_points

        print()
        print("Congratulations " + str(winner[0]) + "! You won this game with " + str(winner[1]) + " points.")

    def print_hand(self, hand):
        output_hand = ""
        for card in hand:
            output_hand += f"({card[0].name}, {card[1].name})" + ", "

        print(output_hand)






skat = Skat()
skat.deal_cards()