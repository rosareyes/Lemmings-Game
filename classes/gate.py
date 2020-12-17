class Gate:
    """ Class for Gate.

    Attributes:
        coordX (int): Coordinate for the columns.
        coordY (int): Coordinate for the rows.
        isActive (bool): keeps track if the tool has been activated by a lemming.
        __sprites (list): list of object's image coordinates into the /assets/lemming.pyxres
            it contains both sprites for entry and exit gates.
            [0]: exit
            [1]: entry
        __isEntry (bool): keeps track whether the object created is an entry gate or an exit gate.
    """
    __coordX: int = 0
    __coordY: int = 0
    __isActive: bool = True
    __sprites = [[32, 32], [16, 32]]
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