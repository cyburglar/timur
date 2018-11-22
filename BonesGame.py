from Bone import Bone

b = "Bones game"

print (b)

bones = [Bone(), Bone(), Bone(), Bone(), Bone()]

for x in bones:
    print (x.throw())

# Зачем тебе три стакана? Если достаточно создать один и бросить его три раза?
# Или по аналогии с костями ... создать массив из трех стаканов
class Glass:
    value = 0
    def __init__(self, contains, throw):
        self.contains = [Bone(), Bone(), Bone(), Bone(), Bone()]
        self.throw = throw

class Glass1:
    value = 0
    def __init__(self, contains, throw):
        self.contains = [Bone(), Bone(), Bone(), Bone(), Bone()]
        self.throw = throw

class Glass2:
    value = 0
    def __init__(self, contains, throw):
        self.contains = [Bone(), Bone(), Bone(), Bone(), Bone()]
        self.throw = throw





