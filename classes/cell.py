class Cell:
    """ Class for Cell: every element in the grid matrix (App.py)
        is made of a object with the Cell class.

    Attributes:
        coordX (int): Coordinate for the columns.
        coordY (int): Coordinate for the rows.
        isActive (bool): keeps track if the tool has been activated by a lemming.
        __sprite (list): list of object's image coordinates into the /assets/lemming.pyxres
    """
    __coordX, __coordY = 0, 0
    __sprite = [0, 28]
    __floor: bool = False
    __tool: object = None
    __gate: object = None

    def __init__(self, y, x):
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

    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, value):
        self.__floor = value

    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, value):
        self.__tool = value

    @property
    def gate(self):
        return self.__gate

    @gate.setter
    def gate(self, value):
        self.__gate = value