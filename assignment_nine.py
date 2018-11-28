# Flint Eller
# 11/16/18
# This program simulates the card game war, called compare
import deck


def create_deck():
    """
    Creates and shuffles deck
    :return: deck of cards
    """
    my_deck = deck.Deck()
    my_deck.shuffle()
    return my_deck


def deal_cards(my_deck):
    """
    Creates empty lists for each player then puts five cards in each
    :param my_deck:
    :return: hand of cards for each player
    """
    user_cards = []
    computer_cards = []
    for a_card in range(5):
        user_cards.append(my_deck.draw_card())
        computer_cards.append(my_deck.draw_card())
    return user_cards, computer_cards


def show_card(user_cards, computer_cards):
    """
    Prints the top card of each player to the screen
    :param user_cards:
    :param computer_cards:
    :return: none
    """
    print("You have a", user_cards)
    print("The computer has a", computer_cards)


def compare(user_cards, computer_cards, user_total, computer_total):
    """
    Gets higher card, says who wins the round and adds a point to that player's total
    :param user_cards:
    :param computer_cards:
    :param user_total:
    :param computer_total:
    :return: the total for each player
    """
    higher_card = user_cards.compare_to(computer_cards)
    if user_cards == higher_card:
        print("You win this round!")
        print("")
        user_total += 1
    else:
        print("The computer wins this round")
        print("")
        computer_total += 1
    return user_total, computer_total


def main():
    user_total = 0
    computer_total = 0
    my_deck = create_deck()
    user_cards, computer_cards = deal_cards(my_deck)
    for x in range(len(user_cards)):
        show_card(user_cards[x], computer_cards[x])
        user_total, computer_total = compare(user_cards[x], computer_cards[x], user_total, computer_total)
    if user_total > computer_total:
        print("You win the game!!!")
    else:
        print("The computer wins the game")


main()
