from lib.deck import Deck


class Sorter:
    def __init__(self, number_of_decks):
        self.all_decks = []
        for i in range(number_of_decks):
            self.all_decks.append(Deck())
