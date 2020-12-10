class Ladder:
    __coordX: int = 0
    __coordY: int = 0
    appearing: bool = False
    # [0]: left
    # [1]: right
    # size 16 x 16
    __sprite: list = [[16,16], [32,16]]
    isActive: bool = True
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