import config


class App:
    __name = None
    __version = None
    __author = None
    __description = None
    __license = None
    __ds = None
    __lang = None

    @staticmethod
    def get_name():
        if App.__name is None:
            App.__name = config.read_params('config/main.ini', 'main')['name']
        return App.__name

    @staticmethod
    def get_version():
        if App.__version is None:
            App.__version = config.read_params('config/main.ini', 'main')['version']
        return App.__version

    @staticmethod
    def get_author():
        if App.__author is None:
            App.__author = config.read_params('config/main.ini', 'main')['author']
        return App.__author

    @staticmethod
    def get_description():
        if App.__description is None:
            App.__description = config.read_params('config/main.ini', 'main')['description']
        return App.__description

    @staticmethod
    def get_license():
        if App.__license is None:
            App.__license = config.read_params('config/main.ini', 'main')['license']
        return App.__license

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
