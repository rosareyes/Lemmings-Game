class Umbrella:
    """ Class for tool: Umbrella.

    Attributes:
        coordX (int): Coordinate for the columns.
        coordY (int): Coordinate for the rows.
        isActive (bool): keeps track if the tool has been activated by a lemming.
        sprite (list): list of object's image coordinates into the /assets/lemming.pyxres size 8x8
    """
    coordX: int = 0
    coordY: int = 0
    __sprite = [[0, 32],[32,64]]
    __isActive: bool = False

    def __init__(self, x, y):
        self.coordX = x
        self.coordY = y

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, value):
        self.__sprite = value

    @property
    def is_active(self):
        return self.__isActive

    @is_active.setter
    def is_active(self, value):
        self.__isActive = value