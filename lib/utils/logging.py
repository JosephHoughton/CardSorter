import logging
import sys


def initialise_logger(config) -> None:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatting = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", "%d-%b-%y %H:%M:%S"
    )
    file_handler = logging.FileHandler(config.log_path)
    file_handler.setFormatter(formatting)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatting)
    logger.addHandler(console_handler)

    logger.info("A new logger has been initialised.")
    logger.info(f"Logger output path set to '{config.log_path}'.")
