from lib.deck import Deck
from random import shuffle
import logging

logger = logging.getLogger("lib.utils.logging")


class Sorter:
    def __init__(self, number_of_decks: int):
        logger.info(f"Creating a new {number_of_decks} deck card sorter...")

        self.all_decks = []
        self.all_cards = []
        for i in range(number_of_decks):
            self.all_decks.append(Deck())

        self.combine_all_decks()
        self.shuffle_all_card()
        logger.info(
            f"Card sorter successfully initialised with {len(self.all_cards)} cards."
        )

    def combine_all_decks(self):
        logger.info("Combining all decks...")
        for deck in self.all_decks:
            self.all_cards.extend(deck.cards)

    def shuffle_all_card(self):
        logger.info("Shuffling all cards from all decks...")
        shuffle(self.all_cards)

    def count_remaining_cards(self):
        remaining_cards = len(self.all_cards)
        logger.info(f"{remaining_cards} cards remaining with the card sorter.")
        return

    def draw_card(self):
        """
        Draw next card from shuffled collection of all cards from all decks. Reset shuffler when final card is drawn.
        """
        try:
            drawn_card = self.all_cards.pop()
            logger.info(f"Card drawn: {drawn_card.value} of {drawn_card.suit}.")
            return
        except IndexError:
            logger.warning("Card sorter has run out of cards.")
            logger.warning("Resetting card sorter...")
            return self.__init__(len(self.all_decks))
