import psycopg2
from flask import Response
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def connect(user, password, host, port):
    try:
        connection = psycopg2.connect(user=user, password=password, host=host, port=port)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return connection

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


class Database:
    def __init__(self, user, password, host, port):
        self.connection = connect(user, password, host, port)

    def execute(self, sql_query, args=(), fetch=False):

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_query, args)
            cursor.close()
            if fetch:
                return cursor.fetchone()
            else:
                return Response(status=200)

        except (Exception, Error) as error:
            return "Ошибка при работе с PostgreSQL" + error
