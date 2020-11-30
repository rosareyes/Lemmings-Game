class Cell:
    __cx, __cy = 0, 0
    __image = ""
    container: list = []  # ["Platform", "Umbrella"]
    # len = no hay platform
    # 1 = hay platform

    def __init__(self, x, y):
        self.__cx = x
        self.__cy = y

    @property
    def x(self):
        return self.__cx

    @x.setter
    def x(self, value):
        self.__cx = value

    @property
    def y(self):
        return self.__cy

    @y.setter
    def y(self, value):
        self.__cy = value

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value