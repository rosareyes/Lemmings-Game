class Lemming:
    """ Class for Lemming.

     Attributes:
         coordX (int): Coordinate for the columns.
         coordY (int): Coordinate for the rows.
         sprites (list): list of object's image coordinates into the /assets/lemming.pyxres
            [0-3]: right lemming movement
            [4-7]: left lemming movement
            [8]: lemming with umbrella
        sprite (list): saves only the sprites' coords of the lemmings' movement in that momement (left or right set)
        sprite_actual (list): has the coords of the actual sprite.
        index (int): allows to change the sprites and make the animation.
        life (bool): tells whether the lemming is dead or alive.
        direction (str): keeps track of the lemmings' direction.
        last_direction (str):  a variable that saves the last direction of the lemming before it goes down.
        falling (bool): tells wether the lemming is falling with an umbrella or no.

    UR: upstairs right
    UL: upstairs left
     """

    __index: int = 0
    __coordX: int
    __coordY: int
    __life: bool = True
    __direction: str
    __ascending: bool = False
    __descending: bool = False
    __last_direction = ""
    __falling: bool = False
    __sprites = [[5, 0], [21, 0], [37, 0], [53, 0], [5, 48], [21, 48], [37, 48], [53, 48], [16, 64]]
    __sprite = [[5, 0], [21, 0], [37, 0], [53, 0]]
    __sprite_actual = [5, 0]

    def __init__(self, x, y, direction):
        self.__coordX = x
        self.__coordY = y
        self.__direction = direction
        self.__sprite_actual = self.__sprite[self.__index]

    @property
    def ascending(self):
        return self.__ascending

    @ascending.setter
    def ascending(self, value):
        self.__ascending = value

    @property
    def falling(self):
        return self.__falling

    @falling.setter
    def falling(self, value):
        self.__falling = value

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
    def sprite_actual(self):
        return self.__sprite_actual

    @sprite_actual.setter
    def sprite_actual(self, value):
        self.__sprite_actual = value

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    @property
    def last_direction(self):
        return self.__last_direction

    @last_direction.setter
    def last_direction(self, value):
        self.__last_direction = value

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, value):
        self.__life = value

    def change_direction(self):
        if self.__direction == "D":
            self.__direction = "S"
        if self.__direction == "R" or self.__direction == "UR":
            self.__direction = "L"
            self.__coordX -= 1
            self.__sprite = [self.__sprites[4], self.__sprites[5], self.__sprites[6], self.__sprites[7]]
        else:
            self.__direction = "R"
            self.sprite = [self.__sprites[0], self.__sprites[1], self.__sprites[2], self.__sprites[3]]

    def walk(self):
        if self.__direction == "R":
            self.__coordX += 1
        elif self.__direction == "L":
            self.__coordX -= 1
        elif self.__direction == "D":
            if self.falling:
                self.__sprite_actual = self.__sprites[8]
            self.__coordY += 1
        elif self.__direction == "UR":
            self.__coordX += 16
            self.__coordY -= 16
        elif self.__direction == "UL":
            self.__coordX -= 16
            self.__coordY -= 16

        if self.__direction == "L" or self.__direction == "R" or self.__direction == "UR":
            self.__index += 1
            if self.__index >= len(self.sprite):
                self.__index = 0
            self.__sprite_actual = self.__sprite[self.index]
