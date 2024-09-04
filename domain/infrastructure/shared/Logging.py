import logging


class Logging:

    def debug(self):
        logging.basicConfig(filename="logs/debug.log", level=logging.DEBUG)
        logging.debug(self)

    def info(self):
        logging.basicConfig(filename="logs/info.log", level=logging.INFO)
        logging.info(self)

    def warning(self):
        logging.basicConfig(filename="logs/warning.log", level=logging.WARNING)
        logging.warning(self)

    def error(self):
        logging.basicConfig(filename="logs/error.log", level=logging.ERROR)
        logging.error(self)

    def critical(self):
        logging.basicConfig(filename="logs/critical.log", level=logging.CRITICAL)
        logging.critical(self)
