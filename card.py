class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit

    def compare_to(self, other_card):
        """
        In this method we are returning the higher card
        :param other_card:
        :return: higher card
        """
        if self.rank > other_card.rank:
            return self
        elif other_card.rank > self.rank:
            return other_card
        else:
            if self.suit > other_card.suit:
                return self
            else:
                return other_card
