from lib.card import Card
from lib.utils import constants


class Deck:
    def __init__(self):
        self.cards = [
            Card(suite, value)
            for value in range(1, constants.HIGHEST_CARD_VALUE)
            for suite in constants.SUITES
        ]
        self.substitute_special_card_names()

    def substitute_special_card_names(self):
        """
        Substitute generic card values for special
        value names (i.e. Jack, Queen, King & Ace)
        """
        for card in self.cards:
            special_value = constants.NAMED_CARDS.get(card.value)
            if special_value:
                card.value = special_value
