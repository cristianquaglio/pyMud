import sys
import psycopg2
from app import App


class DB:

    __conn = None

    @staticmethod
    def __connect__():
        conn = None
        try:
            params = App.get_db_params()
            conn = psycopg2.connect(**params)
        except (Exception, psycopg2.DatabaseError) as error:
            print('Database connection error. Try later, please.')
            sys.exit(1)
        finally:
            return conn

    @staticmethod
    def get_connection():
        if DB.__conn is None:
            DB.__conn = DB.__connect__()
        return DB.__conn

    @staticmethod
    def close_connection():
        if DB.__conn is not None:
            DB.__conn = None
