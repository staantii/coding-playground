from enum import IntEnum
from typing import Tuple, List
import copy

"""
The four colors in skat as an enum. The integer is related to multiplying factor in skat per color
"""
class Colors(IntEnum):
    bells = 2
    hearts = 3
    leaves = 4
    acorns = 5

"""
The different values each color has in skat with the integer of the cards value.
"""
class Values(IntEnum) :
    ace = 11
    ten = 10
    king = 4
    ober = 3
    unter = 2
    nine = 0
    eight = -1
    seven = -2

"""
A card is represented by a tuple of its color and value. For Example: card1 = (leaves, unter)
"""
Card  =  Tuple[Colors, Values]

class Deck:
    def __init__(self):
        self.cards : List[Card] = []
        self.__fill_deck__()

    def __fill_deck__(self):
        for color in Colors:
            for value in Values:
                card = (color, value)
                self.cards.append(card)

    def get_deck(self) -> List[Card]:
        return copy.deepcopy(self.cards)

    def print_deck(self, current_deck: List[Card]):
        output_cards = "All cards:\n"
        for card in current_deck:
            output_cards += f"({card[0].name}, {card[1].name})" + ", "

        print(output_cards)