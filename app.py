import sys
import config


class App:
    __name = ''
    __version = ''
    __author = ''
    __description = ''
    __license = ''
    __ds = ''
    __lang = ''
    __msg_file_error = 'Error reading configuration file. Try later, please.'

    @staticmethod
    def msg_error():
        print(App.__msg_file_error)

    @staticmethod
    def get_name():
        if len(App.__name) is 0:
            try:
                App.__name = config.read_params('config/main.ini', 'main')['name']
            except Exception:
                App.msg_error()
        return App.__name

    @staticmethod
    def get_version():
        if len(App.__version) is 0:
            try:
                App.__version = config.read_params('config/main.ini', 'main')['version']
            except Exception:
                App.msg_error()
        return App.__version

    @staticmethod
    def get_author():
        if len(App.__author) is 0:
            try:
                App.__author = config.read_params('config/main.ini', 'main')['author']
            except Exception:
                App.msg_error()
        return App.__author

    @staticmethod
    def get_description():
        if len(App.__description) is 0:
            try:
                App.__description = config.read_params('config/main.ini', 'main')['description']
            except Exception:
                App.msg_error()
        return App.__description

    @staticmethod
    def get_license():
        if len(App.__license) is 0:
            try:
                App.__license = config.read_params('config/main.ini', 'main')['license']
            except Exception:
                App.msg_error()
        return App.__license

    @staticmethod
    def get_db_params():
        if len(App.__ds) is 0:
            try:
                App.__ds = config.read_params('config/main.ini', 'data_source')
            except Exception:
                App.msg_error()
        return App.__ds

    @staticmethod
    def get_language():
        if len(App.__lang) is 0:
            try:
                App.__lang = config.read_params('config/main.ini', 'location')['language']
            except Exception:
                App.msg_error()
        return App.__lang
