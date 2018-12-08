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
        # здесть должна быть логика
        # три броска ... каждый раз быбираешь кубики ... после 3-х ты должен заполнить один из board
        for y in x :
            print (y)
            list.pop([y]) # QUESTION, sam dobavil, rezultata net
        oneTurn (self) = list(set(glass)) - set([x]) # tut namudril



if __name__== '__main__':   #4to takoe ==
    x = Yahtzee()
    x.oneTurn()
remove_element = 1
if remove_element in list:
    lst.pop(lst.index(remove_element)) # to 4to nashel v nete, ne sovsem ponjal 4to delal











