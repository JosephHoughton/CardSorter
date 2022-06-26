from lib.card import Card


def test_card_creation():
    suit = "Diamond"
    value = 5

    testing_card = Card(suit, value)

    assert type(testing_card) == Card
    assert testing_card.suit == "Diamond"
    assert testing_card.value == 5


def test_card_creation_alternate():
    suit = "Hearts"
    value = 11

    testing_card = Card(suit, value)

    assert type(testing_card) == Card
    assert testing_card.suit == "Hearts"
    assert testing_card.value ==  11
