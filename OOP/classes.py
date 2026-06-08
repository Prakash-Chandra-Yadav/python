##creating the dog class 
class Dog:
    def __init__(self,name,age):
        '''initialize the name and age attributes of the dog'''
        self.name = name
        self.age = age 

    def sit(self):
        '''simulate a dog sitting in a response to a command'''
        print(f"{self.name} is now sitting")
    def roll_over(self):
        ''''simulate rplling in response to a command'''
        print(f"{self.name} is rolling over")
    