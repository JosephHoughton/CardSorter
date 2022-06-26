import logging
from os.path import join
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock

from lib.utils.logging import initialise_logger

logger = logging.getLogger("lib.utils.logging")


def test_setup_log(caplog):
    temp = TemporaryDirectory()
    mock_config = MagicMock()
    test_log_path = join(temp.name, "test.log")
    mock_config.log_path = test_log_path
    initialise_logger(mock_config)

    assert "A new logger has been initialised." in caplog.text
    assert f"Logger output path set to '{test_log_path}'." in caplog.text

    handlers = logger.handlers[:]
    for handler in handlers:
        logger.removeHandler(handler)
        handler.close()
