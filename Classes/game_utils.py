import random

class Dice:

    def __init__(self, num_sides, num_dice):
        self.num_sides = num_sides
        self.num_dice = num_dice

    #return dice values rolled
    def roll(self):
        rolled = []
        for _ in range(self.num_dice):
            r = random.randint(1,self.num_sides)
            rolled.append(r)
        return rolled



if __name__=="__main__":
    d = Dice(16,4)
    print(d.num_sides)
    print(d.num_dice)
    print(d.roll())
