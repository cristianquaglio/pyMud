# -*- coding: utf-8 -*-
import psycopg2
from db import DB


class Player:
    __name = None
    __race = None
    __profession = None
    __level = 0

    def __init__(self, name, race, profession, level=0):
        self.__name = name
        self.__race = race
        self.__profession = profession
        self.__level = level

    def get_name(self):
        return self.__name

    def get_race(self):
        return self.__race

    def get_profession(self):
        return self.__profession

    def get_level(self):
        return self.__level

    def set_name(self, name):
        self.__name = name

    def set_race(self, race):
        self.__race = race

    def set_profession(self, profession):
        self.__profession = profession

    def set_level(self, level):
        self.__level = level

    def __str__(self):
        return self.get_name()

    def save(self):
        result = False
        try:
            sql = '''insert into players (name, race, profession, lvl) values (%s, %s, %s, %s);'''
            conn = DB.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (self.get_name(), self.get_race(), self.get_profession(), self.get_level()))
            conn.commit()
            result = True
        except (Exception, psycopg2.DatabaseError) as error:
            conn.rollback()
        finally:
            return result