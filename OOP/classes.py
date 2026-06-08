# ##creating the dog class 
# class Dog:
#     def __init__(self,name,age):
#         '''initialize the name and age attributes of the dog'''
#         self.name = name
#         self.age = age 

#     def sit(self):
#         '''simulate a dog sitting in a response to a command'''
#         print(f"{self.name} is now sitting")
#     def roll_over(self):
#         ''''simulate rplling in response to a command'''
#         print(f"{self.name} is rolling over")


# ##making an instances from a class 
# my_dog = Dog('Willie',6)

# print(f"my dog name is {my_dog.name}")
# print(f"my dog age is {my_dog.age}")

# ##calling the attributes 
# print(my_dog.name)
# print(my_dog.age)

# ##calling the methods 
# my_dog.sit()
# my_dog.roll_over()

# print("\nCreating the multiple instances")

# my_dog =Dog('williu',9)
# your_dog = Dog('Billie',6)

# print(f"My dog name is my dog {my_dog.name}")
# print(f"your dog name is {your_dog.name}")

# my_dog.sit()
# your_dog.sit()

# my_dog.roll_over()
# your_dog.roll_over()


# print("\nExercises from here")

# ##EXERCISES: 
# #resturant: 
# class Resturant:
#     '''creating the init  function to store the resturent name and the cusine'''
#     def __init__(self,name,cuisine):
#         self.name = name 
#         self.cuisine = cuisine 
#     def describe_resturant(self):
#         print(f"this resturant name is {self.name}")
#         print(f"this resturant serves {self.cuisine}")
#     def open_returant(self):
#         print(f"{self.name} resturant is open now !!")
# ##making and instances from the resturant class 
# my_resturant = Resturant("kfc","chicken")

# ##printing the attributes 
# my_resturant.name 
# my_resturant.cuisine

# #calling the methods 
# my_resturant.describe_resturant()
# my_resturant.open_returant()


# print("\nNext Exercises from here")

# ##three resturants
# my_res = Resturant('rambhandar','sweets')
# your_res = Resturant('kfc','chicken')
# his_res = Resturant('coffeespot','coffee')

# my_res.describe_resturant()
# your_res.describe_resturant()
# his_res.describe_resturant()

# ##USers 
# class User:
#     def __init__(self,first_name,last_name):
#         '''creates the attributes of the first  name and the last name'''
#         self.first_name = first_name 
#         self.last_name = last_name 
#     def describe_user(self):
#         print(f"the users first name is {self.first_name}\n the users last name is {self.last_name}")
#     def greet_user(self):
#         print(f"Hi Mr/Mrs {self.last_name}")
# ##creating the seperate instances and calling the method upon them 
# first_person = User('Prakash','Yadav')
# second_person = User('Albert','Watson')
# third_person = User('Adam','Joseph')

# first_person.describe_user()
# second_person.describe_user()
# third_person.describe_user()

# print("\n")

# first_person.greet_user()
# second_person.greet_user()
# third_person.greet_user()

# ##working with the classes and instances 

# #the car class 
# class Car: 
#     '''a simple attempt to represent a car'''
#     def __init__(self,make,model,year):
#         '''initialize the attributes to describe the car'''
#         self.make = make 
#         self.model = model 
#         self.year = year 
#     def get_discriptive_name(self):
#         '''represent the neatly format descriptive name. '''
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
# my_new_car = Car('audi','a4',2024)
# print(my_new_car.get_discriptive_name())



# print(f"\nSetting a default value for an attribute")
# class Car:
#     def __init__(self,make,model,year):
#         '''initialzie the attributes to describe a car'''
#         self.make = make 
#         self.model = model 
#         self.year = year 
#         self.odometer_reading = 0 

#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name 
#     def read_odometer(self):
#         '''print a statement showing cars milage'''
#         print(f"this car has {self.odometer_reading} miles on it")
# my_car = Car('ford','mustang','year')
# print(my_car.get_descriptive_name())
# my_car.read_odometer()

# ##modifying the attribute values 

# print("\n----MODIFYING ATTRIBUTE VALUES------------")

# print("\n-------modifying an attribute value directly--------")
# class Car: 
#     def __init__(self,make,model,year):
#         self.make = make 
#         self.model = model 
#         self.year = year 
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name 
#     def read_odometer(self):
#         self.odometer_reading = 0 
#     def read_odometer(self):
#         print(f"this car has {self.odometer_reading} miles on it")
# new_car = Car('scorpio','mahindra',2016)
# print(new_car.get_descriptive_name())
# new_car.odometer_reading = 23 
# new_car.read_odometer()


# ##modifying the attributes through method
# print("---------\nModifying an attribute value through a method-----------")

# class Car: 
#     def __init__(self,make,model,year):
#         '''set the default attributes for the car'''
#         self.make = make 
#         self.model = model 
#         self.year = year 
#         self.odometer_reading = 0 
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name 
#     def read_odometer(self):
#         print(f"this car has {self.odometer_reading} miles on it")
#     def update_odometer(self,milage):
#         self.odometer_reading = milage
# another_car = Car('scorpio','mahindra',2016)
# print(another_car.get_descriptive_name())
# another_car.read_odometer()
# another_car.update_odometer(200)
# another_car.read_odometer()

##incrementing an attribute value through a method
print("\n----Incrementing an attribute value through a method------") 
class Car: 
    def __init__(self,make,model,year):
        '''set the default attributes for the car'''
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 20
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name 
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it")
    def increment_odometer(self,milage):
        self.odometer_reading += milage
another_car = Car('scorpio','mahindra',2016)
print(another_car.get_descriptive_name())
another_car.read_odometer()
another_car.increment_odometer(200)
another_car.read_odometer()

##hwo when we directly update the odeo meter reding with the new value which is overriten as the varibale, what if the car owner will roll back the odometer reading by directly updating the value of the odometer reading, how can we prevent that?
print("\n----Preventing the roll back of the odometer reading------")
class Car:
    def __init__(self,make,model,year):


        '''setting the default attributes'''
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 20
    def get_descriptive_name(self):
        print(f"{self.year} {self.make} {self.model}")
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} on it")
    def update_odometer(self,milage):
        if milage > self.odometer_reading:
            self.odometer_reading = milage 
        else: 
            print("sorry you cant roll back the odometer")
old_car = Car('scorpio','mahindra',2026)
old_car.get_descriptive_name()
old_car.read_odometer()
old_car.update_odometer(30)
