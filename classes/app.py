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
    Max_Lemmings = 15
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
    row = int(HEIGHT / 16) # 14
    col = int(WIDTH / 16) # 16

    def __init__(self):
        pyxel.init(self.GAME_WIDTH, self.GAME_HEIGHT, caption="Lemmings' Game")
        pyxel.load("../assets/lemming.pyxres")
        # create matrix
        for i in range(self.row):
            self.grid.append([])
            for j in range(self.col):
                cell = Cell(i, j)
                self.grid[i].append(cell)

        for i in range(self.col):
            if i != 4:
                self.grid[4][i].floor = True


        pyxel.run(self.update, self.draw)

    def exist_floor(self,y,x):
        # for i in self.grid:
        row = int(x / 16)
        col = int(y / 16)
        if self.grid[row][col].floor:
            return True

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
            print("row: {} col: {}".format(row,col))
            umbrella = Umbrella(row, col)
            self.grid[row][col].tool = umbrella
            print(self.grid[row][col].tool.sprite[1])
            # Aqui se debe crear un objeto llamado Umbrella y se añade a la variable "tool"
            print(self.grid[row][col].tool)

        if pyxel.btnp(pyxel.KEY_ENTER):
            row = int((self.sqY - 32) / 16)
            col = int(self.sqX / 16)
            self.grid[col][row].tool = "l"
            print(self.grid[col][row].tool)

        # Lemmings
        if pyxel.frame_count % 50 == 0:
            if self.Max_Lemmings > 0:  # len(list)
                lemming = Lemming(0, 0, "R")
                self.lemmings.append(lemming)
                self.Max_Lemmings -= 1

        # velocity
        if pyxel.frame_count % 1 == 0:
            for lemming in self.lemmings:
                print(lemming.direction)
                if lemming.y < (self.HEIGHT-16) and not self.exist_floor(int(lemming.x), int(lemming.y)):
                    lemming.last_direction=lemming.direction
                    lemming.direction="D"
                elif lemming.direction == "D":
                    lemming.direction="R"

                if lemming.direction == "R":
                    print("lemming.x: ",lemming.x)
                    if lemming.x > self.WIDTH - 16:
                        lemming.changeDirection()
                if lemming.direction == "L":
                    if lemming.x < 0:
                        lemming.changeDirection()
                lemming.walk()

    def draw(self):
        pyxel.cls(1)
        pyxel.text(100, 0, "Lemmings Game", pyxel.frame_count % 16)
        marker = Marker(0, 0, 0, 0, 0, 0, 0)

        # We are printing here our object marker that has a class of marker with all of the game info
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
                #print("{}, {}".format(i, j))
                cell = self.grid[i][j]
                if cell.floor:
                    #print("{}, {}".format(cell.x * 16, cell.y * 16))
                    pyxel.blt((cell.x * 16), (cell.y * 16) + 44, 0, self.grid[i][j].sprite[0], self.grid[i][j].sprite[1], 16, 4, 0)
                if cell.tool:
                    pyxel.blt((cell.x * 16), (cell.y * 16) + 34, 0, self.grid[i][j].tool.sprite[0], self.grid[i][j].tool.sprite[1], 16, 8, 0)
                # print("i: {}, j: {}".format(i, j))
                #pyxel.text(cell.x * 16, (cell.y * 16) + 40, cell.text, 3)
        # pyxel.blt(0, 50, 0, self.lemmings[0].lemming.sprite[0][0], self.lemmings[0].lemming.sprite[0][1], 16, 16, 0)
        pyxel.rectb(self.sqX, self.sqY, 16, 16, 13)

        for lemming in self.lemmings:
            pyxel.blt(lemming.x,lemming.y+28,0,lemming.sprite_actual[0],lemming.sprite_actual[1],16,16,0)

