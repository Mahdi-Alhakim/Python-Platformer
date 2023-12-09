import random

class ground:
    def __init__(self, loc, length):
        self.loc = loc
        self.type = "__ground__"
        self.length = length
        self.array = [[random.randint(self.loc[0], self.loc[0]+self.length-5), random.randint(self.loc[1], self.loc[1]+50)] for i in range(50)]
    def draw(self, cnvs):
        cnvs.create_rectangle(self.loc[0], self.loc[1], self.loc[0]+self.length, self.loc[1]+400, fill="DarkOrange4", outline="DarkOrange4")
        for i in self.array:
            cnvs.create_rectangle(i[0], i[1], i[0]+1, i[1]+1, outline="DarkOrange3")
        cnvs.create_rectangle(self.loc[0], self.loc[1], self.loc[0] + self.length, self.loc[1] + 20, fill="green3", outline="green3")
    def update(self, Xvel, Yvel, env):
        self.loc[0] += Xvel
        self.loc[1] += Yvel
        for i in self.array:
            i[0] += Xvel
            i[1] += Yvel

