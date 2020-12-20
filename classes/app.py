# -*- coding: utf-8 -*-

import pyxel
import random
from classes.lemming import Lemming
from classes.cell import Cell
from classes.umbrella import Umbrella
from classes.blocker import Blocker
from classes.ladder import Ladder
from classes.gate import Gate
from classes.marker import Marker


class App:
    """ Main class where all the logic game is executed.

    Attributes:
        entry_gate (obj):
        exit_gate (obj):
        marker (obj):
        Max_Lemmings (const): maximum number of lemmings.
        MAX_UMBRELLAS (const): maximum number of umbrellas.
        MAX_LADDERS (const): maximum number of ladders.
        MAX_BLOCKERS (const): maximum number of blockers.
        lemmings (list): list of lemmings generated.
        dead_lemmings_list (list): list of dead lemmings.
        saved_lemmings (list): list of saved lemmings.
        MYSIZE (const): the size of every board's square
        sqX, sqY (int): Cursor's coords to select a cell
        GAME_WIDTH, GAME_HEIGHT (const): size of the whole game window.
        WIDTH, HEIGHT (const): size of the game board where the cells are located.
        grid (nested list): this is the matrix where the game is executed.
        color (const): is the color of the background.
        row = (int): the number of rows that the grid has.
        col = (int): the number of cols that the grid has.
        platforms = (list): list of 7 platforms randomly generated.
        sound = (bool): it is used to control wether the sound is on or off.

    """
    level: int = 1
    end_game = False
    next_level = False
    entry_gate: object = None
    exit_gate: object = None
    marker: object = None
    Max_Lemmings: int
    MAX_UMBRELLAS: int
    lemmings_amount: int
    MAX_LADDERS: int
    MAX_BLOCKERS: int
    lemmings = []
    dead_lemmings_list = []
    saved_lemmings = []
    MYSIZE = 16
    sqX, sqY = 0, 32
    GAME_WIDTH, GAME_HEIGHT = 256, 256
    WIDTH, HEIGHT = 256, 224
    grid = []
    color = 3
    row = int(HEIGHT / 16)  # 14
    col = int(WIDTH / 16)  # 16
    platforms = []
    not_floor: bool
    sound = True

    def __init__(self):
        pyxel.init(self.GAME_WIDTH, self.GAME_HEIGHT, caption="Lemmings' Game")
        pyxel.load("../assets/lemming.pyxres")
        pyxel.sound(0).set(
            "f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )

        self.play_music(True, True, True)
        self.reset()
        pyxel.run(self.update, self.draw)

    def play_music(self, ch0, ch1, ch2):
        if ch0:
            pyxel.play(0, [0, 1], loop=True)
        else:
            pyxel.stop(0)

        if ch1:
            pyxel.play(1, [2, 3], loop=True)
        else:
            pyxel.stop(1)

        if ch2:
            pyxel.play(2, 4, loop=True)
        else:
            pyxel.stop(2)

    def reset(self):
        """Initiate key variables"""
        self.MAX_UMBRELLAS = 5
        self.MAX_BLOCKERS = 5
        self.MAX_LADDERS = 8
        self.Max_Lemmings = 15
        self.not_floor = True
        self.platforms = []
        self.grid = []
        self.lemmings = []
        self.dead_lemmings_list = []
        self.saved_lemmings = []
        self.lemmings_amount = self.Max_Lemmings

        if not self.end_game and self.next_level:
            self.level += 1
        else:
            self.level = 1

        self.end_game = False
        self.next_level = False
        self.marker = Marker(self.level, 0, 0, 0, 0, 0, 0)

        # create matrix
        for i in range(self.row):
            self.grid.append([])
            for j in range(self.col):
                cell = Cell(i, j)
                self.grid[i].append(cell)

        # Creating the platform list random with validations
        for i in range(0, 7):
            repeated = True
            width = random.randint(5, 10)
            while repeated:
                y = random.randint(0, 12)
                y_list = []
                if self.platforms:
                    for platform in self.platforms:
                        y_list.append(platform[1])
                    if y in y_list:
                        repeated = True
                    else:
                        repeated = False
                else:
                    repeated = False
            xrepeated = True
            while xrepeated:
                x = random.randint(0, 11)
                if x + width >= 16:
                    xrepeated = True
                else:
                    xrepeated = False
            self.platforms.append([width, y, x])

        # adding the platforms into the cells
        for platform in self.platforms:
            for i in range(platform[0]):
                # print("Y: ",platform[1])
                # print("X: ", platform[2]+i)
                self.grid[platform[1]][platform[2] + i].floor = True

        # create exit door random
        while self.not_floor:
            y = random.randint(0, 13)
            x = random.randint(0, 15)
            if self.exist_floor(x * 16, y * 16):
                self.exit_gate = Gate(y, x, False)
                self.grid[y][x].gate = self.exit_gate
                self.not_floor = False
            else:
                self.not_floor = True

        # create entry door random
        self.not_floor = True
        while self.not_floor:
            y = random.randint(0, 13)
            x = random.randint(0, 15)
            if self.exist_floor(x * 16, y * 16) and not self.exist_exit_gate(x * 16, y * 16):
                self.entry_gate = Gate(y, x, True)
                self.grid[y][x].gate = self.entry_gate
                self.not_floor = False
            else:
                self.not_floor = True

    def exist_floor(self, x, y):
        row = int(y / 16)
        col = int(x / 16)
        if self.grid[row][col].floor:
            return True

    def exist_exit_gate(self, x, y):
        row = int(y / 16)
        col = int(x / 16)
        if isinstance(self.grid[row][col].gate, Gate):
            if not self.grid[row][col].gate.is_entry:
                return True
        return False

    def have_umbrella(self, x, y):
        row = int(y / 16)
        col = int(x / 16)
        if isinstance(self.grid[row][col].tool, Umbrella):
            return True
        else:
            return False

    def have_ladder(self, x, y):
        row = int(y / 16)
        col = int(x / 16)
        if isinstance(self.grid[row][col].tool, Ladder):
            return True
        else:
            return False

    def have_blocker(self, x, y):
        row = int(y / 16)
        col = int(x / 16)
        if isinstance(self.grid[row][col].tool, Blocker):
            return True
        else:
            return False

    def update(self):
        if pyxel.btnp(pyxel.KEY_ENTER):
            self.reset()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_S):
            if self.sound:
                self.play_music(False, False, False)
                self.sound = False
            else:
                print("entre")
                self.play_music(True, True, True)
                self.sound = True
        # Cursor's movement
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.sqX + 16 <= self.WIDTH - 16:
                self.sqX += 16
        if pyxel.btnp(pyxel.KEY_LEFT):
            if self.sqX - 16 >= 0:
                self.sqX -= 16
        if pyxel.btnp(pyxel.KEY_DOWN):
            print(self.sqY)
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
            instance = isinstance(self.grid[row][col].tool, Umbrella)
            if instance:
                self.grid[row][col].tool = None
                self.MAX_UMBRELLAS += 1
                self.marker.umbrellas_value -= 1

            if self.MAX_UMBRELLAS > 0 and not instance:
                # print("row: {} col: {}".format(row,col))
                umbrella = Umbrella(row, col)
                self.grid[row][col].tool = umbrella
                self.marker.umbrellas_value += 1
                self.MAX_UMBRELLAS -= 1

        # Left Ladder
        if pyxel.btnp(pyxel.KEY_L):
            row = int((self.sqY - 32) / 16)
            col = int(self.sqX / 16)
            instance = isinstance(self.grid[row][col].tool, Ladder)
            if instance:
                self.grid[row][col].tool = None
                self.MAX_LADDERS += 1
                self.marker.ladders_value -= 1
            if self.MAX_LADDERS > 0 and not instance:
                ladder = Ladder(row, col, "left")
                self.grid[row][col].tool = ladder
                self.marker.ladders_value += 1
                self.MAX_LADDERS -= 1

        # Right Ladder
        if pyxel.btnp(pyxel.KEY_K):
            row = int((self.sqY - 32) / 16)
            col = int(self.sqX / 16)
            instance = isinstance(self.grid[row][col].tool, Ladder)
            if instance:
                self.grid[row][col].tool = None
                self.MAX_LADDERS += 1
                self.marker.ladders_value -= 1
            if self.MAX_LADDERS > 0 and not instance:
                ladder = Ladder(row, col, "right")
                self.grid[row][col].tool = ladder
                self.marker.ladders_value += 1
                self.MAX_LADDERS -= 1

        # Blocker
        if pyxel.btnp(pyxel.KEY_B):
            row = int((self.sqY - 32) / 16)
            col = int(self.sqX / 16)
            instance = isinstance(self.grid[row][col].tool, Blocker)
            if instance:
                self.grid[row][col].tool = None
                self.MAX_BLOCKERS += 1
                self.marker.blockers_value -= 1
            if self.MAX_BLOCKERS > 0 and not instance and self.exist_floor(col * 16, row * 16):
                blocker = Blocker(row, col)
                self.grid[row][col].tool = blocker
                self.marker.blockers_value += 1
                self.MAX_BLOCKERS -= 1

        """Determinate whether the game is over or the user is going to the next level"""
        if not self.lemmings and self.marker.died_value == self.lemmings_amount:
            self.end_game = True
        if self.marker.saved_value + self.marker.died_value == self.lemmings_amount:
            self.next_level = True

        """Creating Lemmings with the entry gate as a starting point"""
        if pyxel.frame_count % 60 == 0:
            if self.Max_Lemmings > 0:  # len(list)
                lemming = Lemming((self.entry_gate.x * 16), (self.entry_gate.y * 16), "R")
                self.lemmings.append(lemming)
                self.Max_Lemmings -= 1
                self.marker.alive_value += 1

        """the frame count reduces the speed of the lemmings' movement"""
        if pyxel.frame_count % 1 == 0:
            """
            This functions is to keep track not only of the lemming object but also it's index
            To pop it out the list later
            """
            for i, lemming in enumerate(self.lemmings):
                if self.have_ladder(int(lemming.x), int(lemming.y)) and self.exist_floor(int(lemming.x), int(lemming.y)):
                    if not self.grid[int(lemming.y/16)][int(lemming.x/16)].tool.is_active:
                        self.grid[int(lemming.y / 16)][int(lemming.x / 16)].tool.is_active = True
                    lemming.ascending = False
                    """if the lemming is going right and the ladder is for the left, it will ignore it and vice versa"""
                    if lemming.direction == "R" and self.grid[int(lemming.y / 16)][
                        int(lemming.x / 16)].tool.direction == "right":
                        lemming.direction = "UR"
                    elif lemming.direction == "L" and self.grid[int(lemming.y / 16)][
                        int(lemming.x / 16)].tool.direction == "left":
                        lemming.direction = "UL"
                elif self.exist_floor(int(lemming.x), int(lemming.y)) and lemming.direction == "UR":
                    lemming.ascending = False
                    lemming.direction = "R"
                elif self.exist_floor(int(lemming.x), int(lemming.y)) and lemming.direction == "UL":
                    lemming.ascending = False
                    lemming.direction = "L"

                if self.have_blocker(int(lemming.x), int(lemming.y)):
                    if not self.grid[int(lemming.y/16)][int(lemming.x/16)].tool.is_active:
                        self.grid[int(lemming.y / 16)][int(lemming.x / 16)].tool.is_active = True
                    lemming.change_direction()
                """If the cell doesn't have a ladder and doesn't have floor, it will change direction"""
                if lemming.y < (self.HEIGHT - 16) and not self.exist_floor(int(lemming.x), int(lemming.y)) and not self.have_ladder(int(lemming.x), int(lemming.y)):
                    if lemming.direction == "L":
                        lemming.x -= 4
                    lemming.direction = "D"
                    """If our lemming touches an umbrella, its falling attribute is set to true"""
                    if self.have_umbrella(int(lemming.x), int(lemming.y)):
                        if not self.grid[int(lemming.y / 16)][int(lemming.x / 16)].tool.is_active:
                            self.grid[int(lemming.y / 16)][int(lemming.x / 16)].tool.is_active = True
                        lemming.falling = True
                elif lemming.direction == "D" and lemming.falling:
                    lemming.falling = False
                    lemming.direction = "R"
                    if lemming.last_direction == "R":
                        lemming.direction = "R"
                    elif lemming.last_direction == "L":
                        lemming.direction = "L"

                if lemming.direction == "R":
                    if lemming.direction != "D":
                        lemming.last_direction = lemming.direction
                    if lemming.x >= self.WIDTH - 6:
                        lemming.change_direction()

                if lemming.direction == "L":
                    if lemming.direction != "D":
                        lemming.last_direction = lemming.direction
                    if lemming.x < 0:
                        lemming.change_direction()

                # saved lemmings
                if self.exist_exit_gate(int(lemming.x), int(lemming.y)):
                    saved_lemming = self.lemmings.pop(i)
                    self.saved_lemmings.append(saved_lemming)
                    self.marker.saved_value = len(self.saved_lemmings)

                # lemmings' death
                if (lemming.y == (self.HEIGHT - 16) and not self.exist_floor(int(lemming.x), int(lemming.y))) or (lemming.direction == "D" and not lemming.falling and self.exist_floor(int(lemming.x), int(lemming.y))):
                    lemming.life = False
                    dead_lemming = self.lemmings.pop(i)
                    self.dead_lemmings_list.append(dead_lemming)
                    self.marker.died_value = len(self.dead_lemmings_list)
                    self.marker.alive_value -= 1
                lemming.walk()

    def draw(self):
        """
        Three scenarios:
        1. If the game is starting
        2. If the user loses
        3. If the user goes to the next level.
        """

        if not self.end_game and not self.next_level:
            pyxel.cls(0)
            pyxel.text(100, 0, "Lemmings Game", pyxel.frame_count % 16)
            pyxel.text(0, 245, "blockers: B  umbrella: SPACE  ladders: L/K  sound: S  quit: Q", 14)

            # We are printing here our object marker that has a class of marker with all of the game info
            pyxel.text(30, 10, "{}".format(self.marker.level), 7)
            pyxel.text(55, 10, "{}".format(self.marker.level_value), 6)
            pyxel.text(80, 10, "{}".format(self.marker.alive), 7)
            pyxel.text(105, 10, "{}".format(self.marker.alive_value), 6)
            pyxel.text(130, 10, "{}".format(self.marker.saved), 7)
            pyxel.text(155, 10, "{}".format(self.marker.saved_value), 6)
            pyxel.text(180, 10, "{}".format(self.marker.died), 7)
            pyxel.text(203, 10, "{}".format(self.marker.died_value), 6)
            pyxel.text(40, 20, "{}".format(self.marker.ladders), 7)
            pyxel.text(75, 20, "{}".format(self.marker.ladders_value), 6)
            pyxel.text(90, 20, "{}".format(self.marker.umbrellas), 7)
            pyxel.text(132, 20, "{}".format(self.marker.umbrellas_value), 6)
            pyxel.text(160, 20, "{}".format(self.marker.blockers), 7)
            pyxel.text(200, 20, "{}".format(self.marker.blockers_value), 6)

            # drawing the matrix
            for i in range(self.row):
                for j in range(self.col):
                    cell = self.grid[i][j]
                    if cell.floor:
                        pyxel.blt((cell.x * 16), (cell.y * 16) + 44, 0, self.grid[i][j].sprite[0],
                                  self.grid[i][j].sprite[1], 16, 4, 0)
                    if cell.tool:
                        if isinstance(cell.tool, Ladder):
                            if cell.tool.direction == "left":
                                if cell.tool.is_active:
                                    pyxel.blt((cell.x * 16), (cell.y * 16) + 28, 0, self.grid[i][j].tool.sprite[0][0],
                                              self.grid[i][j].tool.sprite[0][1], 16, 16, 0)
                                else:
                                    pyxel.blt((cell.x * 16), (cell.y * 16) + 28, 0, self.grid[i][j].tool.sprite[2][0],
                                              self.grid[i][j].tool.sprite[2][1], 16, 16, 0)
                            elif cell.tool.direction == "right":
                                if cell.tool.is_active:
                                    pyxel.blt((cell.x * 16), (cell.y * 16) + 28, 0, self.grid[i][j].tool.sprite[1][0],
                                              self.grid[i][j].tool.sprite[1][1], 16, 16, 0)
                                else:
                                    pyxel.blt((cell.x * 16), (cell.y * 16) + 28, 0, self.grid[i][j].tool.sprite[3][0],
                                              self.grid[i][j].tool.sprite[3][1], 16, 16, 0)
                        if isinstance(cell.tool, Umbrella):
                            if cell.tool.is_active:
                                pyxel.blt((cell.x * 16), (cell.y * 16) + 32, 0, self.grid[i][j].tool.sprite[0][0],
                                          self.grid[i][j].tool.sprite[0][1], 16, 8, 0)
                            else:
                                pyxel.blt((cell.x * 16), (cell.y * 16) + 32, 0, self.grid[i][j].tool.sprite[1][0],
                                          self.grid[i][j].tool.sprite[1][1], 16, 8, 0)
                        if isinstance(cell.tool, Blocker):
                            if cell.tool.is_active:
                                pyxel.blt((cell.x * 16), (cell.y * 16) + 32, 0, self.grid[i][j].tool.sprite[0][0],
                                          self.grid[i][j].tool.sprite[0][1], 16, 12, 0)
                            else:
                                pyxel.blt((cell.x * 16), (cell.y * 16) + 32, 0, self.grid[i][j].tool.sprite[1][0],
                                          self.grid[i][j].tool.sprite[1][1], 16, 12, 0)
                    if cell.gate:
                        if cell.gate.is_entry:
                            pyxel.blt((cell.x * 16), (cell.y * 16) + 32, 0, self.grid[i][j].gate.sprites[1][0],
                                      self.grid[i][j].gate.sprites[1][1], 16, 12, 0)
                        elif not cell.gate.is_entry:
                            pyxel.blt((cell.x * 16), (cell.y * 16) + 32, 0, self.grid[i][j].gate.sprites[0][0],
                                      self.grid[i][j].gate.sprites[0][1], 16, 12, 0)

            """Drawing our cursors' square """
            pyxel.rectb(self.sqX, self.sqY, 16, 16, 13)

            """Drawing our lemmings"""
            for lemming in self.lemmings:
                if lemming.falling:
                    if lemming.last_direction == "L":
                        pyxel.blt(lemming.x - 12, lemming.y + 28, 0, lemming.sprite_actual[0], lemming.sprite_actual[1], 16,
                                  16, 0)
                    else:
                        pyxel.blt(lemming.x, lemming.y + 28, 0, lemming.sprite_actual[0], lemming.sprite_actual[1], 16, 16,
                                  0)
                else:
                    pyxel.blt(lemming.x, lemming.y + 28, 0, lemming.sprite_actual[0], lemming.sprite_actual[1], 6, 16, 0)

            """To draw the blood when a lemming dies."""
            for dead_lemming in self.dead_lemmings_list:
                if self.exist_floor(dead_lemming.x, dead_lemming.y):
                    pyxel.blt(dead_lemming.x, dead_lemming.y + 42, 0, 0, 74, 16, 6, 0)
                else:
                    pyxel.blt(dead_lemming.x, dead_lemming.y + 46, 0, 0, 74, 16, 6, 0)

        elif self.end_game:
            pyxel.cls(0)
            pyxel.text(60, 130, "AW! ALL OF YOUR LEMMINGS DIED! :(", 6)
            pyxel.text(100, 140, "GAME OVER", 6)
            pyxel.text(60,150,"PRESS ENTER TO RESTART THE GAME",6)

        if self.next_level and not self.end_game:
            pyxel.cls(0)
            if self.marker.alive_value == self.lemmings_amount:
                pyxel.text(60, 130, "WOW! YOU SAVED THEM ALL!", 6)
            else:
                pyxel.text(60, 130, "COOL! YOU SAVED SOME OF THEM!", 6)
            pyxel.text(60, 150, "PRESS ENTER TO GO TO NEXT LEVEL", 6)