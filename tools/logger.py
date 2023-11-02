import functools
import logging

from flask import request

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

    def request_log(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                self.info(' ' + request.method + ' ' + request.url)
                return func(*args, **kwargs)
            except Exception as error:
                self.error(str(error))
        return wrapper
