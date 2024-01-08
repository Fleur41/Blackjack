'''
Blackjack
-------------------------------------------------------------
'''

import random
import os

class Card:
    def __init__(self, card_face, value, symbol) -> None:
        self.card_face = card_face
        self.value = value
        self.symbol = symbol