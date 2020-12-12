class Gate:
    __coordX: int = 0
    __coordY: int = 0
    # 0: exit
    # 1: entry
    __sprites = [[32,32],[16,32]]
    # To ask: when Lemmings go into Exit Gate,
    # does it need to have an Active atribute to know
    # when Lemmings reach it?
    __isActive: bool = True
    __isEntry: bool = False

    def __init__(self, y, x, entry):
        self.__coordX = x
        self.__coordY = y
        self.__isEntry = entry

    @property
    def x(self):
        return self.__coordX

    @x.setter
    def x(self, value):
        self.__coordX = value

    @property
    def y(self):
        return self.__coordY

    @y.setter
    def y(self, value):
        self.__coordY = value

    @property
    def is_entry(self):
        return self.__isEntry

    @is_entry.setter
    def is_entry(self, value):
        self.__isEntry = value

    @property
    def sprites(self):
        return self.__sprites

    @sprites.setter
    def sprites(self, value):
        self.__sprites = value