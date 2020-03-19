class Player:
    __name = None
    __race = None
    __profession = None
    __level = 0

    def __init__(self, name, race, profession, level):
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