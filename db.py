import psycopg2
import config


class DB:

    __conn = None

    @staticmethod
    def get_connection():
        if DB.__conn is None:
            DB.__conn = DB.__connect__()
        return DB.__conn

    @staticmethod
    def __connect__():
        conn = None
        try:
            params = config.read_params('config/main.ini', 'data_source')
            conn = psycopg2.connect(**params)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            return conn

    @staticmethod
    def close_connection():
        if DB.__conn is not None:
            DB.__conn = None
