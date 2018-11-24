from Bone import Bone


class Glass:
    value = []
    def __init__(self):
        self.bones = [Bone(), Bone(), Bone(), Bone(), Bone()]
    def throw(self):
        z = []
        for x in self.bones:
            z.append(x.throw())
        return z
    def remove(self, x):
        del self.bones[0:x]

class Yahtzee:
    board = {}
    board["1"] = []
    board["2"] = []
    board["3"] = []
    board["4"] = []
    board["5"] = []
    board["6"] = []
    def oneTurn (self):
        glass = Glass()
        x = glass.throw()
        for y in x :
            print (y)






if __name__== '__main__':
    x = Yahtzee()
    x.oneTurn()

