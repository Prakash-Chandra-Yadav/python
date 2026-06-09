from random import randint,choice 
class Dice: 
    def __init__(self,side):
        self.side = side 
    def roll_dice(self):
        for  x in range(1,11):
            face = randint(1,self.side)
            print(face)
d1 = Dice(6)
d1.roll_dice()
