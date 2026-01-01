"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card."""
    if card in ('J', 'Q', 'K'):
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one == value_two:
        return card_one, card_two
    elif value_one > value_two:
        return card_one
    else:
        return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card."""

    # Count existing cards, treating any ace already in hand as 11
    def card_value(card):
        if card in ('J', 'Q', 'K'):
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)

    total = card_value(card_one) + card_value(card_two)

    if total + 11 <= 21:
        return 11
    else:
        return 1



def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""
    has_ace = card_one == 'A' or card_two == 'A'
    has_ten_value = value_of_card(card_one) == 10 or value_of_card(card_two) == 10

    return has_ace and has_ten_value


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)
