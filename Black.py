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

def show_cards(cards, hidden):
    s = ''
    for card in cards:
        s = s + '\t ________________'
    if hidden:
        s += '\t ________________'