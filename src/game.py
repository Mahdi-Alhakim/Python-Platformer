from tkinter import *

from player import player
from ground import ground


class game:
    def __init__(self, master, cnvs):
        self.master = master
        self.canvas = cnvs

        self.environment = [ground([i*200, 200], 200) for i in range(-1, 2)]

        #playerInfo
        self.camLoc = [100, 100]

        self.plyrs = [player(self.master, [100, 100], "blue"), player(self.master, [300, 100], "red")]

        self.frameSpeed = 15
        self.speedFactor = 400.0/self.frameSpeed

        for i in self.plyrs:
            i.drawPlayer(self.canvas)

        #BIND KEYS
        self.master.bind("<Key>", self.keydown)
        self.master.bind("<KeyRelease>", self.keyup)
        self.master.bind("<Key-q>", lambda x : self.plyrs[0].shoot(self.environment, self.canvas, self.plyrs, x))

        self.master.bind("<Up>", self.up)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Left>", self.left)
        self.master.bind("<KeyRelease-Right>", self.rightUp)
        self.master.bind("<KeyRelease-Left>", self.leftUp)
        self.master.bind("<Key-m>", lambda x: self.plyrs[1].shoot(self.environment, self.canvas, self.plyrs, x))

        self.main()
    def keydown(self, e):
        print(e.char)
        if e.char=="e":
            self.plyrs[0].jump(self.environment);return
        if e.char=="f":
            self.plyrs[0].plyrVel[0] = 0
            self.plyrs[0].plyrVel[0] = 10
            self.plyrs[0].dir = 1
        if e.char=="s":
            self.plyrs[0].plyrVel[0] = 0
            self.plyrs[0].plyrVel[0] = -10
            self.plyrs[0].dir = -1
    def keyup(self, e):
        if e.char == "f" and self.plyrs[0].plyrVel[0] > 0: self.plyrs[0].plyrVel[0] = 0
        if e.char == "s" and self.plyrs[0].plyrVel[0] <= 0: self.plyrs[0].plyrVel[0] = 0

    def up(self, e): self.plyrs[1].jump(self.environment)
    def right(self, e):
        self.plyrs[1].plyrVel[0] = 0
        self.plyrs[1].plyrVel[0] = 10
        self.plyrs[1].dir = 1
    def left(self, e):
        self.plyrs[1].plyrVel[0] = 0
        self.plyrs[1].plyrVel[0] = -10
        self.plyrs[1].dir = -1
    def rightUp(self, e):
        if self.plyrs[1].plyrVel[0] > 0: self.plyrs[1].plyrVel[0] = 0
    def leftUp(self, e):
        if self.plyrs[1].plyrVel[0] <= 0: self.plyrs[1].plyrVel[0] = 0

    def updateCam(self):
        Xchange = 0#(self.plyrLoc[0] - self.camLoc[0])
        Ychange = 0#(self.plyrLoc[1] - self.camLoc[1])
        self.camLoc = (self.camLoc[0]+Xchange, self.camLoc[1]+Ychange)
        return (Xchange, Ychange)

    def draw(self):
        self.canvas.delete("all")

        for i in self.plyrs:
            i.drawPlayer(self.canvas)
        for i in self.environment:
            i.draw(self.canvas)
        self.canvas.create_text(20, 10, text=str(self.plyrs[0].health))
        self.canvas.create_text(380, 10, text=str(self.plyrs[1].health))



    def main(self):
        for i in self.plyrs:
            i.updatePlayer(self.environment, self.speedFactor)
        #change = self.updateCam()
        for i in self.environment:
            change = 0, 0#self.plyrVel[0], 0
            i.update(-change[0], -change[1], self.environment)



        self.draw()
        self.master.after(self.frameSpeed, self.main)


