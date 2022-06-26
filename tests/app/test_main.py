import sys

from app.main import parse_arguments


def test_main():
    test_log_path = "test\\path"
    test_number_of_decks = "5"
    args = ["-l", test_log_path, "-n", test_number_of_decks]
    sys.argv[1:] = args
    test_config = parse_arguments()

    assert test_log_path == str(test_config.log_path)
    assert test_number_of_decks == str(test_config.number_of_decks)
