from app.sorter import Sorter
from mock import patch


def test_single_deck_sorter():
    testing_sorter = Sorter(1)

    assert len(testing_sorter.all_decks) == 1
    assert len(testing_sorter.all_cards) == len(set(testing_sorter.all_cards))
    assert len(testing_sorter.all_cards) == 52


def test_multi_deck_sorter():
    testing_sorter = Sorter(3)

    assert len(testing_sorter.all_decks) == 3
    assert len(testing_sorter.all_cards) == len(set(testing_sorter.all_cards))
    assert len(testing_sorter.all_cards) == 156


def test_draw_card():
    testing_sorter = Sorter(1)
    assert len(testing_sorter.all_cards) == 52

    testing_sorter.draw_card()
    assert len(testing_sorter.all_cards) == 51

    testing_sorter.draw_card()
    assert len(testing_sorter.all_cards) == 50


def test_sorter_reset():
    testing_sorter = Sorter(1)
    for i in range(52):
        testing_sorter.draw_card()

    with patch("app.sorter.Sorter.__init__") as sorter_init_mock:
        testing_sorter.draw_card()
        assert sorter_init_mock.called
