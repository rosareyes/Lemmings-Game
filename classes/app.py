import pyxel
from classes.lemming import Lemming
from classes.cell import Cell
from classes.umbrella import Umbrella
from classes.blocker import Blocker
from classes.ladder import Ladder
from classes.gate import Gate
from classes.marker import Marker


class App:
    MAX_SUELOS = 3
    Max_Lemmings = 20
    lemmings = []
    x = 0
    # MYSIZE: the size of every board's square
    MYSIZE = 16
    # Cursor's coords to select a cell
    sqX, sqY = 0, 32
    GAME_WIDTH, GAME_HEIGHT = 256, 256
    WIDTH, HEIGHT = 256, 224
    grid = []
    color = 3
    # we add 16 in order for the matrix to draw all of it
    # bc for some reason the last one of the row doesn't get drawn
    row = int(HEIGHT / 16) + 16
    col = int(WIDTH / 16)

    def __init__(self):
        pyxel.init(self.GAME_WIDTH, self.GAME_HEIGHT, caption="Lemmings' Game")
        pyxel.load("../assets/lemming.pyxres")

        # create matrix
        for i in range(self.row):
            self.grid.append([])
            for j in range(self.col):
                cell = Cell(i, j)
                # cell.image = str("s")
                self.grid[i].append(cell)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # Cursor's movement
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
        # Drawing on the board
        if pyxel.btnp(pyxel.KEY_SPACE):
            # We translate cursor's position (pyxels) to the matrix -> Cell
            # We subtract 32 to sqY because it's where the board starts
            # (the 32 spaces up are occupied by the board's marker)
            row = int((self.sqY - 32) / 16)
            col = int(self.sqX / 16)
            self.grid[col][row].image = "U"
            self.grid[col][row].container[1] = "Umbrella"
            # Aqui se debe crear un objeto llamado Umbrella y se añade al container
            # print(self.grid[col][row].container[1])

        if pyxel.btnp(pyxel.KEY_ENTER):
            row = int((self.sqY - 32) / 16)
            col = int(self.sqX / 16)
            print("enter: ", row, col)
            self.grid[col][row].image = "L"
            self.grid[col][row].container[1] = "Ladder"
            print(self.grid[col][row].container[1])

        # Lemmings
        if pyxel.frame_count % 50 == 0: # que es esto?
            if self.Max_Lemmings > 0:  # len(list)
                lemming = Lemming(0, 32, "R")
                self.lemmings.append(lemming)
                self.Max_Lemmings -= 1

        # velocity
        if pyxel.frame_count % 5 == 0:
            for lemming in self.lemmings:
                lemming.walk()
                if lemming.direction == "R":
                    if lemming.x > self.WIDTH - 16:
                        lemming.changeDirection()
                if lemming.direction == "L":
                    if lemming.x < 0:
                        lemming.changeDirection()

    def draw(self):
        pyxel.cls(1)
        pyxel.text(100, 0, "Lemmings Game", pyxel.frame_count % 16)
        marker = Marker(0, 0, 0, 0, 0, 0, 0)

        pyxel.text(30, 10, "{}".format(marker.level), 7)
        pyxel.text(55, 10, "{}".format(marker.level_value), 6)
        pyxel.text(80, 10, "{}".format(marker.alive), 7)
        pyxel.text(105, 10, "{}".format(marker.alive_value), 6)
        pyxel.text(130, 10, "{}".format(marker.saved), 7)
        pyxel.text(155, 10, "{}".format(marker.saved_value), 6)
        pyxel.text(180, 10, "{}".format(marker.died), 7)
        pyxel.text(203, 10, "{}".format(marker.died_value), 6)
        pyxel.text(40, 20, "{}".format(marker.ladders), 7)
        pyxel.text(75, 20, "{}".format(marker.ladders_value), 6)
        pyxel.text(90, 20, "{}".format(marker.umbrellas), 7)
        pyxel.text(132, 20, "{}".format(marker.umbrellas_value), 6)
        pyxel.text(160, 20, "{}".format(marker.blockers), 7)
        pyxel.text(200, 20, "{}".format(marker.blockers_value), 6)

        # drawing the matrix
        for i in range(self.row):
            for j in range(self.col):
                cell = self.grid[i][j]
                pyxel.blt((cell.x * 16), (cell.y * 16) + 48, 0, 0, 28, 16, 4, 0)
                pyxel.text(cell.x * 16, (cell.y * 16) + 40, cell.image, 3)
        # pyxel.blt(0, 50, 0, self.lemmings[0].lemming.sprite[0][0], self.lemmings[0].lemming.sprite[0][1], 16, 16, 0)
        pyxel.rectb(self.sqX, self.sqY, 16, 16, 13)
        # drawing a door:
        # pyxel.blt(self.sqX, self.sqY, 0, 16, 32, 16, 16, 0)

        for lemming in self.lemmings:
            pyxel.blt(lemming.x,lemming.y,0,lemming.sprite_actual[0],lemming.sprite_actual[1],16,16,0)

    # def test_blt(self, x, y):
    #
    #     # lemming.sprite[0] = lemming.sprites[0]
    #     # lemming.sprite[1] = lemming.sprites[1]
    #     # pyxel.blt(lemming.x,lemming.y,0,lemming.sprite[0][0],lemming.sprite[0][1],16,16,0)
    #     pyxel.rectb(x, y, 16, 16, 13)
    #     pyxel.blt(x, y, 0, 16, 32, 16, 16, 0)
    #     # drawing a blocker
    #     # pyxel.blt(x, y+8, 0, 0, 16, 16, 8, 0)
    #     # drawing a ladder
    #     # pyxel.blt(x, y, 0, 16, 16, 16, 16, 0)
    #     # drawing a lemming
    #     # pyxel.blt(x, y, 0, 0, 0, 16, 16, 0)