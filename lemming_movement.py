import pyxel
import time


class Lemming:
    __index: int = 0
    __coordX: int = 0
    __coordY: int = 0
    __life: bool = True
    __direction: str = "R"
    # or "left"
    __ascending: bool = False
    __descending: bool = False
    __falling: bool = False
    # 0: 0,0 Lemming R
    # 1: 16, 0 Lemming R
    # 3: 32, 0 Lemming R
    # 4: 48, 0 Lemming R
    # 5: 0, 48 Lemming L
    # 6: 16,48 Lemming L
    __sprites = [[0, 0], [16, 0], [32, 0],[48, 0], [0, 48], [16, 48], [32,48],[48,48]]
    __sprite=[[0, 0], [16, 0], [32, 0], [48, 0]]
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

    def cambiarDireccion(self):
        if self.__direction == "R":
            self.__direction = "L"
            self.__sprite = [self.__sprites[4], self.__sprites[5],self.__sprites[6],self.__sprites[7]]
        else:
            self.__direction = "R"
            self.sprite = [self.__sprites[0], self.__sprites[1],self.__sprites[2],self.__sprites[3]]

    def avanzar(self):
        if self.__direction == "R":
            self.__coordX += 1
        else:
            self.__coordX -= 1
        self.__index += 1
        if self.__index >= len(self.sprite):
            self.__index = 0
        # cómo hacer que se muevan más lento?
        self.__sprite_actual = self.__sprite[self.index]

    def avanzarR(self):
        self.__coordX += 1

    def avanzarL(self):
        self.__coordX -= 1



class Cell:
    __cx, __cy = 0, 0
    __image = ""
    container: list = ["", ""]  # ["Platform", "Umbrella"]

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


class App:
    Max_Lemmings = 20
    lemmings = []
    x = 0
    MYSIZE = 16
    sqX, sqY = 0, 32  # Coordenadas cursor para seleccionar celda
    GAME_WIDTH, GAME_HEIGHT = 256, 256
    WIDTH, HEIGHT = 256, 224
    grid = []
    color = 3
    fila = int(HEIGHT / 16) + 16 # añado 16 para que se dibuje toda la matriz bc for some reason no se dibuja el ultimo de la fila
    columna = int(WIDTH / 16)

    stop = fila
    step = 1
    stop += step  # now stop is 6

    def __init__(self):
        pyxel.init(self.GAME_WIDTH, self.GAME_HEIGHT, caption="Pyxel Lemmings")
        pyxel.load("assets/lemming.pyxres")
        # 0,0 Lemming R
        # 16, 0 Lemming R
        # 0, 48 Lemming L
        # 16,48 Lemming L

        # create matrix
        for i in range(self.fila):
            self.grid.append([])
            for j in range(self.columna):
                cell = Cell(i, j)
                # cell.image = str("s")
                self.grid[i].append(cell)
        pyxel.run(self.update, self.draw)

    def update(self):

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # Movimientos rectangulo
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.sqX + 16 <= self.WIDTH - 16:
                self.sqX += 16
        if pyxel.btnp(pyxel.KEY_LEFT):
            if self.sqX - 16 >= 0:
                self.sqX -= 16
        if pyxel.btnp(pyxel.KEY_DOWN):
            if (self.sqY - 32) + 16 <= self.HEIGHT - 16:
                self.sqY += 16
        if pyxel.btnp(pyxel.KEY_UP):
            if (self.sqY - 32) - 16 >= 0:
                self.sqY -= 16

        # DIBUJO EN TABLERO
        if pyxel.btnp(pyxel.KEY_SPACE):
            # traducir posicion del cursor (pyxels) a la matrix -> Cell
            row = int((self.sqY - 32) / 16)
            col = int(self.sqX / 16)
            print("sqY: ",self.sqY)
            print("space",row,col)
            self.grid[col][row].image = "U"
            self.grid[col][row].container[1] = "Umbrella"
            #Aqui se crea un objeto llamado Umbrella y se añade al container
            print(self.grid[col][row].container[1])
        # se le resta 32 porque es donde realmente empieza el tablero (los 32 espacios de arriba estan ocupados por las letras)
        if pyxel.btnp(pyxel.KEY_ENTER):
            row = int((self.sqY - 32) / 16)
            col = int(self.sqX / 16)
            print("enter: ",row, col)
            self.grid[col][row].image = "L"
            self.grid[col][row].container[1] = "Ladder"
            print(self.grid[col][row].container[1])
        # Lemmings
        if pyxel.frame_count % 50 == 0: # que es esto?

            if self.Max_Lemmings > 0:  # len(list)

                lemming = Lemming(0, 32, "R")
                # print("hey ", lemming)
                self.lemmings.append(lemming)
                self.Max_Lemmings -= 1

        for lemming in self.lemmings:
            lemming.avanzar()
            if lemming.direction == "R":
                if lemming.x > self.WIDTH - 16:
                    lemming.cambiarDireccion()

            if lemming.direction == "L":
                if lemming.x < 0:
                    lemming.cambiarDireccion()

    def draw(self):
        pyxel.cls(1)
        pyxel.text(0, 0, "                      Lemmings Game", pyxel.frame_count % 16)
        pyxel.text(0, 10, "Level:", 7)
        pyxel.text(50, 10, "Alive:", 7)
        pyxel.text(100, 10, "Saved:", 7)
        pyxel.text(150, 10, "Died:", 7)
        pyxel.text(0, 20, "Ladders:", 7)
        pyxel.text(70, 20, "Umbrellas:", 7)
        pyxel.text(140, 20, "Blockers:", 7)
        # pyxel.rect(self.sqX, self.sqY, 16, 16, 1)

        # drawing the matrix
        for i in range(self.fila):
            for j in range(self.columna):
                cell = self.grid[i][j]
                pyxel.blt((cell.x * 16), (cell.y * 16) + 48, 0, 0, 28, 16, 4, 0)
                pyxel.text(cell.x * 16, (cell.y * 16) + 40, cell.image, 3)
        # pyxel.blt(0, 50, 0, self.lemmings[0].lemming.sprite[0][0], self.lemmings[0].lemming.sprite[0][1], 16, 16, 0)
        self.test_blt(self.sqX, self.sqY)
        for lemming in self.lemmings:
            # print("hey ", lemming.sprite_actual)
            pyxel.blt(lemming.x,lemming.y,0,lemming.sprite_actual[0],lemming.sprite_actual[1],16,16,0)

    def test_blt(self, x, y):

        # lemming.sprite[0] = lemming.sprites[0]
        # lemming.sprite[1] = lemming.sprites[1]
        # pyxel.blt(lemming.x,lemming.y,0,lemming.sprite[0][0],lemming.sprite[0][1],16,16,0)
        pyxel.rectb(x, y, 16, 16, 13)
        pyxel.blt(x, y, 0, 16, 32, 16, 16, 0)
        # drawing a blocker
        # pyxel.blt(x, y+8, 0, 0, 16, 16, 8, 0)
        # drawing a ladder
        # pyxel.blt(x, y, 0, 16, 16, 16, 16, 0)
        # drawing a lemming
        # pyxel.blt(x, y, 0, 0, 0, 16, 16, 0)


App()
