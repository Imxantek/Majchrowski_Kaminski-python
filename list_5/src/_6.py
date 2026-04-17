import logging
from logging import StreamHandler, Logger
import sys

class LessThanErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno < logging.ERROR

stdout = StreamHandler(sys.stdout)
stderr = StreamHandler(sys.stderr)

formatter = logging.Formatter('[%(levelname)s]: %(message)s')

stdout.setFormatter(formatter)
stderr.setFormatter(formatter)

stdout.addFilter(LessThanErrorFilter())
stdout.setLevel(logging.DEBUG)

stderr.setLevel(logging.ERROR)
logger = Logger("_5.py")
logger.setLevel(logging.DEBUG)
logger.addHandler(stdout)
logger.addHandler(stderr)
