class Umbrella:
    coordX: int = 0
    coordY: int = 0
    appearing: bool = False
    __sprite = [0, 32]
    # size 8x8
    falling: bool = False
    isActive: bool = True

    def __init__(self, x, y):
        self.coordX = x
        self.coordY = y

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, value):
        self.__sprite = value
