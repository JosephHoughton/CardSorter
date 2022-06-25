from lib.deck import Deck
from lib.card import Card
from unittest.mock import MagicMock


def test_deck_object_creation():
    testing_deck = Deck()

    assert all(isinstance(card, Card) for card in testing_deck.cards)
    assert len(testing_deck.cards) == 52


def test_subbing_special_card_names():
    testing_deck = Deck()
    mock_card_1 = MagicMock()
    mock_card_1.value = 1

    mock_card_2 = MagicMock()
    mock_card_2.value = 5

    mock_card_3 = MagicMock()
    mock_card_3.value = 11

    mock_card_4 = MagicMock()
    mock_card_4.value = 13

    testing_deck.cards = [mock_card_1, mock_card_2, mock_card_3, mock_card_4]
    testing_deck.substitute_special_card_names()

    assert mock_card_1.value == "Ace"
    assert mock_card_2.value == 5
    assert mock_card_3.value == "Jack"
    assert mock_card_4.value == "King"
