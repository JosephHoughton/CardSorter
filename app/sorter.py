from lib.deck import Deck
from random import shuffle


class Sorter:
    def __init__(self, number_of_decks):
        self.all_decks = []
        self.all_cards = []
        for i in range(number_of_decks):
            self.all_decks.append(Deck())

        self.combine_all_decks()
        self.shuffle_all_card()

    def combine_all_decks(self):
        for deck in self.all_decks:
            self.all_cards.extend(deck.cards)

    def shuffle_all_card(self):
        shuffle(self.all_cards)

    def draw_card(self):
        try:
            return print(f"Card drawn: {self.all_cards.pop()}")
        except IndexError:
            self.__init__(len(self.all_decks))
