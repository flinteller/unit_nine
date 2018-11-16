import card
import random


class Deck:

    def __init__(self):

        self.card_deck = []
        for rank in range(13):
            for suit in range(4):
                new_card = card.Card(rank, suit)
                self.card_deck.append(new_card)

    def draw_card(self):
        new_card = self.card_deck.pop()
        return new_card

    def shuffle(self):
        random.shuffle(self.card_deck)
