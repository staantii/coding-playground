import random

from player import *

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

        # the moves get evaluated and a winner (I know it's supposed to be looser but eh) is determined
        winner = self.evaluate(self.current_round_cards, color)
        winner.get_all_cards(self.current_round_cards)
        self.current_round_cards.clear()

        # on the last round the winner gets the skat
        if last_round:
            winner.get_skat(self.skat)

        # the player order for the next round is determined
        new_player_order = self.get_player_order(winner, player_order)
        return new_player_order

    def get_player_order(self, winner, player_order):
        # sets the new player order
        new_player_order = []
        index_of_winner = 0

        # first we search for the index of the winner
        for i in range(0, len(player_order)):
            if player_order[i][0] == winner:
                index_of_winner = i

        # now we shift the order so the winner starts and then we go around clockwise
        new_player_order.append(player_order[index_of_winner])
        new_player_order.append(player_order[(index_of_winner+1)%3])
        new_player_order.append(player_order[(index_of_winner+2)%3])

        return new_player_order


    def evaluate(self, who_played_what, color):
        # initializing the moves
        first_move = who_played_what[0]
        second_move = who_played_what[1]
        third_move = who_played_what[2]

        best_move = first_move

        # evaluating which move is the best
        best_move = self.compare_two_cards(color, best_move, second_move)
        best_move = self.compare_two_cards(color, best_move, third_move)

        print()
        print(str(best_move[0].name) + " gets all cards from this round! They played: (" + str(best_move[1][0].name) + ", " + str(best_move[1][1].name) + ").")

        return best_move[0]

    def compare_two_cards(self, color, best_move, move2):
        # changes the best move to the second move if either
        # they're the same color and the second move has a higher value
        # OR both moves are trumps but the color of the second move values higher
        # OR the second move is an unter but the first move isn't
        if (move2[1][0] == color and move2[1][1] > best_move[1][1]) \
                or (move2[1][1] == 2 and best_move[1][0] == 2 and move2[1][0] > best_move[1][0]) \
                or (move2[1][1] == 2 and best_move[1][1] != 2):
            best_move = move2

        return best_move


    def player_move(self, player, hand, color = None):
        # simulates one move from one player

        # first of all we check if the player has a valid card to play or if the player is the first of their round
        has_a_valid_card = False
        init_color = False

        if color is None:
        # if color is none, the player is the first one to play and therefor can decide on a color
            init_color = True
            pass
        elif not color:
        # if color is false, the player plays a trump round and can only lay unter
            for card in hand:
                if card[1] == 2:
                    has_a_valid_card = True
        else:
        # if the player's not the first one and there is a color, all our cards with the specific color are valid
            for card in hand:
                if card[0] == color and card[1] != 2:
                    has_a_valid_card = True

        # now starting the move
        print(str(player.name) + "s turn! You have the following cards: ")
        self.print_hand(hand)
        print()

        while True:
            # player decides on a card. the card gets checked if it's a valid move. if not they have to try again
            index = input("Enter the number of the card you would like to play: ")
            index = int(index) - 1
            card_to_play = hand[index]
            print(card_to_play)

            # checking that if the player has a valid card, they also play it
            if has_a_valid_card and (card_to_play[0] == color or card_to_play[1] == 2):
                break

            # if the player is the first one to play they decide on a color or if they play a trump round
            elif init_color:
                if card_to_play[1] == 2:
                    color = False
                    break
                color = card_to_play[0]
                break

            # if the player neither has a valid card nor an unter they can play whatever
            elif not has_a_valid_card and not init_color:
                break
            else:
                print("You have a valid card. Please play it.")

        hand.remove(card_to_play)

        new_tuple = (player, card_to_play)

        self.current_round_cards.append(new_tuple)
        return color

    def calculate_winner(self, player1, player2, player3):
        # first of all we calculate the points of every player
        player1_points = player1.get_points()
        player2_points = player2.get_points()
        player3_points = player3.get_points()

        winner = player1_points
        # now we compare the points to see who has the less points
        if player2_points[1] < winner[1]:
            winner = player2_points

        if player3_points[1] < winner[1]:
            winner = player3_points

        print()
        print("Congratulations " + str(winner[0]) + "! You won this game with " + str(winner[1]) + " points.")

    def print_hand(self, hand):
        output_hand = ""
        i = 1
        for card in hand:
            output_hand += f"{i}: ({card[0].name}, {card[1].name})" + ", "
            i += 1

        print(output_hand)

