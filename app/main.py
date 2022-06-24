import sys
from app.sorter import Sorter


def main():
    sorter = Sorter(2)
    sorter.draw_card()


if __name__ == "__main__":
    sys.exit(main())
