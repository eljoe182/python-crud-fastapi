import logging
import sys


class LoggerObserver:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        formatter = logging.Formatter(
            fmt="[%(asctime)s] %(name)s:%(process)d | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        stream_handler = logging.StreamHandler(sys.stdout)
        file_handler = logging.FileHandler("app.log", encoding="utf-8")

        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.handlers = [stream_handler, file_handler]

    def info(self, message: str) -> None:
        self.logger.setLevel(logging.INFO)
        self.logger.info(message)

    def error(self, message: str) -> None:
        self.logger.setLevel(logging.ERROR)
        self.logger.error(message)

    def warning(self, message: str) -> None:
        self.logger.setLevel(logging.WARNING)
        self.logger.warning(message)

    def debug(self, message: str) -> None:
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug(message)

    def critical(self, message: str) -> None:
        self.logger.setLevel(logging.CRITICAL)
        self.logger.critical(message)
