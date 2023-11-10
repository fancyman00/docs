import functools
import logging

from flask import Response

from tools.singelton import Singleton


class Logger(metaclass=Singleton):
    def __init__(self, app):
        self.app = app
        logging.basicConfig(filename='logger.log')

    def error(self, msg: str):
        self.app.logger.error(msg)

    def warning(self, msg: str):
        self.app.logger.warning(msg)

    def info(self, msg: str):
        self.app.logger.info(msg)

    def request(self, msg='Request Log'):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    self.info(f' {msg}')
                    return func(*args, **kwargs)
                except Exception as error:
                    self.error(str(error))
                    raise error

            return wrapper

        return decorator
