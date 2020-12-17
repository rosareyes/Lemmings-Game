class Blocker:
    """ Class for tool: Blocker.

    Attributes:
        coordX (int): Coordinate for the columns.
        coordY (int): Coordinate for the rows.
        isActive (bool): keeps track if the tool has been activated by a lemming.
        __sprite (list): list of object's image coordinates into the /assets/lemming.pyxres
    """

    coordX: int = 0
    coordY: int = 0
    appearing: bool = False
    isActive: bool = True
    __sprite: list = [0,16]

    def __init__(self, x, y):
        self.__coordX = x
        self.__coordY = y

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
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, value):
        self.__sprite = value

