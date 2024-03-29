import psycopg2
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

    def execute(self, sql_query, args=(), fetch=False, count=False):

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql_query, args)
                result = None
                if fetch:
                    if count:
                        result = cursor.fetchmany(int(count))
                    else:
                        result = cursor.fetchall()
                else:
                    result = ''
                return result

        except (Exception, Error) as error:
            raise Exception("Ошибка при работе с PostgreSQL: " + str(error))
