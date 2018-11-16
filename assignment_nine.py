# Flint Eller
# 11/16/18
# This program simulates the card game war, called compare

import card
import deck


def create_deck():
    my_deck = deck.Deck()
    my_deck.shuffle()
    return my_deck


def deal_cards(my_deck):
    user_cards = []
    computer_cards = []
    for a_card in range(5):
        user_cards.append(my_deck.draw_card())
        computer_cards.append(my_deck.draw_card())
    return user_cards, computer_cards


def main():
    my_deck = create_deck()
    deal_cards(my_deck)
    show_card()
    compare()
    winner()

main()
