import unittest
from ..deck import *


class TestDeck(unittest.TestCase):
    def test_right_length_of_deck(self):
        deck = Deck()

        "A deck has always 32 cards:"
        right_length = 32
        self.assertEqual(right_length, len(deck.deck), "The deck is not initialised right.")



if __name__ == '__main__':
    unittest.main()
