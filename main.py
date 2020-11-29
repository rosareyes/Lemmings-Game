# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:39:31 2019

@authors: Rosa Reyes, Paloma Núñez
@version: 1.0
"""

import pyxel


class Cell:
    cx=0
    cy=3

    def __init__(self,x,y):
        self.cx=x
        self.cy=y
        self.image=""

        pyxel.image(1).load(0, 0, "assets/cat_16x16.png")

class App:
    GAME_WIDTH = 256
    GAME_HEIGHT = 256
    WIDTH = 128
    HEIGHT = 160
    CAPTION = "Lemming's Project"
    color = 3
    fila = int(WIDTH/16)
    columna = int(HEIGHT/16)
    grid=[]
    x = 0
    sqX, sqY = 0, 30


    def __init__(self):
        pyxel.init(self.GAME_WIDTH, self.GAME_HEIGHT, caption=self.CAPTION)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_RIGHT):
            if self.sqX+16<=self.WIDTH-16:
                self.sqX+=16
        if pyxel.btnp(pyxel.KEY_LEFT):
            if self.sqX-16>=0:
                self.sqX-=16
        if pyxel.btnp(pyxel.KEY_DOWN):
            if self.sqY+16<=self.HEIGHT-16:
                self.sqY+=16
        if pyxel.btnp(pyxel.KEY_UP):
            if self.sqY-16>=30:
                self.sqY-=16
    def draw(self):
        pyxel.cls(self.color)
        pyxel.text(0, 0, "                      Lemmings Game", pyxel.frame_count % 16)
        pyxel.text(0, 10, "Level:", 7)
        pyxel.text(50, 10, "Alive:", 7)
        pyxel.text(100, 10, "Saved:", 7)
        pyxel.text(150, 10, "Died:", 7)
        pyxel.text(0, 20, "Ladders:", 7)
        pyxel.text(70, 20, "Umbrellas:", 7)
        pyxel.text(140, 20, "Blockers:", 7)
        pyxel.rect(self.sqX,self.sqY,16,16,1)
        self.test_blt(6, 88)
    def test_blt(self, x, y):
        y += 15
        pyxel.blt(x + 38, y, 1, 0, 0, -16, 16, 13)
        pyxel.blt(x, y, 0, 0, 0, 16, 16,13)


App()
