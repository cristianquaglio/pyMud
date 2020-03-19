from configparser import ConfigParser


def read_params(filename, section):
    parser = ConfigParser()
    parser.read(filename)
    pms = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            pms[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return pms