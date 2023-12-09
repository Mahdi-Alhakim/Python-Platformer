import tkinter.messagebox
from projectile import projectile

class player:
    def __init__(self, root, loc, color="white"):
        self.root = root
        self.color = color

        self.plyrLoc = loc
        self.plyrVel = [0, 0]
        self.gravity = 9.8
        self.plyrCanJump = True
        self.health = 100

        self.dir = 1


    def drawPlayer(self, cnvs):
        self.obj = cnvs.create_oval(self.plyrLoc[0]-15, self.plyrLoc[1]-15, self.plyrLoc[0]+15, self.plyrLoc[1]+15, fill=self.color)

    def updatePlayer(self, env, speed):
        self.plyrLoc[0] += self.plyrVel[0]
        if self.plyrVel[1] > 0:
            for i in env:
                if i.type=="__ground__" and i.loc[0]-5 < self.plyrLoc[0] < i.loc[0]+i.length+5 and self.plyrLoc[1]+15 >= i.loc[1]:
                    self.plyrLoc[1] = i.loc[1]-15
                    self.plyrVel[1] = 0
                    self.plyrCanJump = True
                    return
        self.plyrLoc[1] += self.plyrVel[1]
        self.plyrVel[1] += self.gravity/speed

    def jump(self, env):
        for i in env:
            if i.type=="__ground__" and i.loc[0] - 5 < self.plyrLoc[0] < i.loc[0] + i.length + 5 and self.plyrLoc[1] + 15 >= i.loc[1]:
                self.plyrVel[1] = -6
                return
        if self.plyrCanJump:
            self.plyrVel[1] = -6
            self.plyrCanJump = False

    def shoot(self, env, cnvs, plyrs, e):
        env += [projectile(self.plyrLoc, self.dir, cnvs, self.obj, plyrs, color=self.color)]

    def takeDamage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.root.destroy()
            tkinter.messagebox.showinfo("GAMEOVER", "<{}> lost!".format(self.color))
