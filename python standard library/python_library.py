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


class Lottery: 
    def __init__(self,*combinations):
        self.combinations = combinations
    def create_lottery(self):
        lottery = [] 
        for i in range(1,5):
            character = choice(self.combinations)
            lottery.append(character)
        self.see_lottry(lottery)
        return lottery
            
    def see_lottry(self,lottery):
        print("any ticked matching these 4 numbers or letter wins the prize: ")
        for char in lottery:
            print(char,end='')
            
l1 = Lottery(1,4,5,6,8,8,5,3,1,'a','b','c','d','e','f')
winning_ticket = l1.create_lottery()
Lottery_range = (1,4,5,6,8,8,5,3,1,'a','b','c','d','e','f')
attempts = 0 
while True: 
    my_ticket = []
    for i in range(1,5):
        choice_number = choice(Lottery_range)
        my_ticket.append(choice_number)
    if my_ticket == winning_ticket:
        print("you win the lottery")
        print(f"-----you won the lottery, you have tried {attempts} times-----")
        break
    else:
        attempts += 1
        print(f"you lose the lottery, you have tried {attempts} times")


    



