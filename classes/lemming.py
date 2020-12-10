class Lemming:
    __index: int = 0
    __coordX: int = 0
    __coordY: int = 0
    __life: bool = True
    __direction: str = "R"
    # or "left"
    __ascending: bool = False
    __descending: bool = False
    __last_direction = ""
    __falling: bool = False
    # 0: 0,0 Lemming R
    # 1: 16, 0 Lemming R
    # 3: 32, 0 Lemming R
    # 4: 48, 0 Lemming R
    # 5: 0, 48 Lemming L
    # 6: 16,48 Lemming L
    __sprites = [[0, 0], [16, 0], [32, 0], [48, 0], [0, 48], [16, 48], [32, 48], [48, 48]]
    __sprite = [[0, 0], [16, 0], [32, 0], [48, 0]]
    __sprite_actual = [0, 0]

    def __init__(self, x, y, direction):
        self.__coordX = x
        self.__coordY = y
        self.__direction = direction
        self.__sprite_actual = self.__sprite[self.__index]

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
    def life(self):
        return self.__life

    @life.setter
    def life(self, value):
        self.__life = value

    def changeDirection(self):
        if self.__direction == "D":
            self.__direction = "S"
        if self.__direction == "R":
            self.__direction = "L"
            self.__sprite = [self.__sprites[4], self.__sprites[5],self.__sprites[6],self.__sprites[7]]
        else:
            self.__direction = "R"
            self.sprite = [self.__sprites[0], self.__sprites[1],self.__sprites[2],self.__sprites[3]]

    def walk(self):
        if self.__direction == "R":
            self.__coordX += 1
            #print("Entro a walk R, mi coord X: ", self.__coordX)
        elif self.__direction == "L":
            #print("Entro a walk, mi coord X: ",self.__coordX)
            self.__coordX -= 1
        elif self.__direction == "D":
            self.__coordY+=1
        elif self.__direction=="US":
            self.__coordY-=4
            self.__coordX+=4
        elif self.__direction=="DS":
            self.y+=16
            self.x+=16

        if self.__direction=="L" or self.__direction=="R":
            self.__index += 1
            if self.__index >= len(self.sprite):
                self.__index = 0
            self.__sprite_actual = self.__sprite[self.index]

    def avanzarR(self):
        self.__coordX += 1

    def avanzarL(self):
        self.__coordX -= 1