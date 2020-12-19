class Ladder:
    """ Class for tool: Ladder.

    Attributes:
        coordX (int): Coordinate for the columns.
        coordY (int): Coordinate for the rows.
        isActive (bool): keeps track if the tool has been activated by a lemming.
        sprite (list): list of object's image coordinates into the /assets/lemming.pyxres
            it contains both sprites for left and right ladders. size 16 x 16
            [0]: left
            [1]: right
        direction (str): it tells whether the object created is a right or a left ladder.
    """
    __coordX: int = 0
    __coordY: int = 0
    __sprite: list = [[16,16], [32,16], [48,64], [0,80]]
    __isActive: bool = False
    __direction: str = "right"

    def __init__(self, x, y, dire):
        self.__coordX = x
        self.__coordY = y
        self.__direction = dire

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, value):
        self.__sprite = value

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    @property
    def is_active(self):
        return self.__isActive

    @is_active.setter
    def is_active(self, value):
        self.__isActive = value