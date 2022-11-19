import logging
import sys


def configure_logging(level=logging.INFO):
    logging.basicConfig(level=level, stream=sys.stdout)
