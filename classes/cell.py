class Cell:
    __cx, __cy = 0, 0
    __sprite = [0, 28]
    __floor: bool = False
    __tool: object = None
    __text = "s"

    #__container = [""]  # ["p", "Umbrella"]
    # len = no hay platform
    # 1 = hay platform

    def __init__(self, y, x):
        self.__cx = x
        self.__cy = y

    @property
    def x(self):
        return self.__cx

    @x.setter
    def x(self, value):
        self.__cx = value

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    @property
    def y(self):
        return self.__cy

    @y.setter
    def y(self, value):
        self.__cy = value

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, value):
        self.__sprite = value

    # @property
    # def container(self):
    #     return self.__container
    #
    #
    # @container.setter
    # def container(self, value):
    #     self.__container[0] = value

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