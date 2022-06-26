import argparse
import logging
import pathlib
import sys

from app.sorter import Sorter
from lib.utils.logging import initialise_logger

logger = logging.getLogger("lib.utils.logging")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Arguments required to run sorter programme."
    )
    parser.add_argument(
        "-l", "--log_path", required=True, type=pathlib.Path, help="Log output path."
    )
    parser.add_argument(
        "-n",
        "--number_of_decks",
        dest="number_of_decks",
        type=int,
        default=1,
        help="Number of decks to include in sorter.",
    )
    return parser.parse_args()


def initialise_programme():
    config = parse_arguments()
    initialise_logger(config)

    return config


def run_sorter(config):
    sorter = Sorter(config.number_of_decks)
    sorter.draw_card()
    sorter.count_remaining_cards()
    sorter.reset_sorter()
    for i in range(260):
        sorter.draw_card()

    sorter.count_remaining_cards()
    sorter.draw_card()


def main():
    config = initialise_programme()
    run_sorter(config)
    logger.info("Card sorter terminated successfully.")


if __name__ == "__main__":
    sys.exit(main())
