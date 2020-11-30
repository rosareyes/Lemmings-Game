# Do we need to do a class for the game board values?
# Died, Alive, Lemmings...
# Marker


class Marker:
    __level: str = "Level: "
    __level_value: int = 0
    __alive: str = "Alive: "
    __alive_value: int = 0
    __saved: str = "Saved: "
    __saved_value: int = 0
    __died: str = "Died: "
    __died_value: int = 0
    __ladders: str = "Ladders: "
    __ladder_value: int = 0
    __umbrellas: str = "Umbrellas: "
    __umbrellas_value: int = 0
    __blockers: str = "Blockers: "
    __blockers_value: int = 0

    def __init__(self, level, alive, saved, died, ladders, umbrellas, blockers):
        self.__level_value = level
        self.__alive_value = alive
        self.__saved_value = saved
        self.__died_value = died
        self.__ladders_value = ladders
        self.__umbrellas_value = umbrellas
        self.__blockers_value = blockers

    # Getters for the game board's text
    @property
    def level(self):
        return self.__level

    @property
    def alive(self):
        return self.__alive

    @property
    def saved(self):
        return self.__saved

    @property
    def died(self):
        return self.__died

    @property
    def ladders(self):
        return self.__ladders

    @property
    def umbrellas(self):
        return self.__umbrellas

    @property
    def blockers(self):
        return self.__blockers

    @property
    def level_value(self):
        return self.__level_value

    @level_value.setter
    def level_value(self, value):
        self.__level_value = value

    @property
    def alive_value(self):
        return self.__alive_value

    @alive_value.setter
    def alive_value(self, value):
        self.__alive_value = value

    @property
    def saved_value(self):
        return self.__saved_value

    @saved_value.setter
    def saved_value(self, value):
        self.__saved_value = value

    @property
    def died_value(self):
        return self.__died_value

    @died_value.setter
    def died_value(self, value):
        self.__died_value = value

    @property
    def ladders_value(self):
        return self.__ladders_value

    @ladders_value.setter
    def ladders_value(self, value):
        self.__ladders_value = value

    @property
    def umbrellas_value(self):
        return self.__umbrellas_value

    @umbrellas_value.setter
    def umbrellas_value(self, value):
        self.__umbrellas_value = value

    @property
    def blockers_value(self):
        return self.__blockers_value

    @blockers_value.setter
    def level_value(self, value):
        self.__blockers_value = value
