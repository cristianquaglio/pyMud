import sys
from configparser import ConfigParser


def read_params(filename, section):
    pms = {}
    try:
        parser = ConfigParser()
        parser.read(filename)
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                pms[param[0]] = param[1]
    except Exception:
        print('Filesystem error. Try later, please.')
        sys.exit(1)
    return pms
