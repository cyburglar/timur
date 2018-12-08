from Bone import Bone


class Glass:
    value = []

    def __init__(self):
        self.bones = [Bone(), Bone(), Bone(), Bone(), Bone()]

    def throw(self, bonesLeft = 5):
        z = []
        #Выбор из 5 или оставшихся костей
        for x in self.bones[0:bonesLeft]:
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

    def turn(self, bonesLeft = 5):
        #бросаешь имено столько сколько в bonesLeft
        glass = Glass()
        x = glass.throw(bonesLeft)
        for y in x:
            print (y)
        return x


if __name__ == '__main__':  # 4to takoe ==
    x = Yahtzee()
    bones = x.turn()
    #здесь отсортировать и выбрать совподающие числа ... остальные перебросить.
