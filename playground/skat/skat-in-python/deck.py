from enum import IntEnum
from typing import Tuple

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
        self.deck = []
        self.__fill_deck__()

    def __fill_deck__(self):
        for color in Colors:
            for value in Values:
                card = (color, value)
                self.deck.append(card)



deck = Deck()