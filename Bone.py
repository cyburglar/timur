import random


class Bone:
    value = 0

    @staticmethod
    def throw():
        return random.randint(1, 6)
