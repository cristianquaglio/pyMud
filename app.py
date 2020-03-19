import config


class App:
    __ds = None
    __lang = None

    @staticmethod
    def get_db_params():
        if App.__ds is None:
            App.__ds = config.read_params('config/main.ini', 'data_source')
        return App.__ds

    @staticmethod
    def get_language():
        if App.__lang is None:
            App.__lang = config.read_params('config/main.ini', 'location')['language']
        return App.__lang
