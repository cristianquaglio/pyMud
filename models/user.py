# -*- coding: utf-8 -*-
import psycopg2
from db import DB


class User:
    __email = None
    __pass  = None

    def __init__(self, email, passwd):
        self.__email = email
        self.__pass = passwd

    def get_email(self):
        return self.__email

    def get_passwd(self):
        return self.__pass

    def set_email(self, email):
        self.__email = email

    def set_passwd(self, passwd):
        self.__pass = passwd

    def save(self):
        result = False
        try:
            sql = '''insert into users (email, password) values (%s, %s);'''
            conn = DB.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (self.get_email(), self.get_passwd()))
            conn.commit()
            result = True
        except (Exception, psycopg2.DatabaseError) as error:
            conn.rollback()
        finally:
            return result
