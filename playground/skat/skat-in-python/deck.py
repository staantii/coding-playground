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
    eight = 0
    seven = 0

"""
A card is represented by a tuple of its color and value. For Example: card1 = (leaves, unter)
"""
Card  =  Tuple[Colors, Values]

class Deck:
    def __init__(self):
        self.deck = []


deck = Deck()