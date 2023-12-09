class projectile:
    def __init__(self, loc, dir, canvas, obj, plyrs, size=20, speed=20, color="red"):
        self.loc = list(loc)
        self.size = size
        self.dir = dir
        self.cnvs = canvas
        self.speed = speed
        self.color = color
        self.obj, self.plyrs = obj, plyrs
        self.type = "__bullet__"
    def update(self, Xvel, Yvel, env):
        self.loc[0]+=self.dir*self.speed+Xvel
        self.loc[1]+=Yvel

        ovrlp = self.cnvs.find_overlapping(self.loc[0], self.loc[1], self.loc[0]+self.size, self.loc[1]+self.size/10.0)
        for i in ovrlp:
            for _ in self.plyrs:
                if _.obj==i and i!= self.obj:
                    _.takeDamage(self.size/4)
                    env.remove(self)
                    return


    def draw(self, cnvs):
        cnvs.create_rectangle(self.loc[0], self.loc[1], self.loc[0]+self.size, self.loc[1]+self.size/10.0, fill = self.color, outline=self.color)
