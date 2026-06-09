##create the electric car class from the car class
class Car:
    def __init__(self,make,model,year):
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0
    def get_descriptive_name(self): 
        print(f"{self.year} {self.make} {self.model}")
    def read_odometer(self):
        '''read the odometer'''
        print(f"this car has {self.odometer_reading} miles on it")
    def update_odometer(self,milage):
        '''update the odometer'''
        if milage > self.odometer_reading:
            self.odometer_reading = milage 
        else: 
            print("you cant roll back the odometer")
    def increment_odometer(self,milage):
        '''increment the odometer value by the given number'''
        self.odometer_reading += milage 
    def fill_gas_tank(self):
        print("filled the gas tank")
# class ElectricCar(Car):
#     '''represents the aspects of the car, specifice to electriv vehicles'''
#     def __init__(self,make,model,year):
#         '''initialize attributes of the oarent class '''
#         super().__init__(make,model,year)

# ##lets check if our child class is working or not 
# my_leaf = ElectricCar('nissan','leaf',2024)
# my_leaf.get_descriptive_name()




print("\nDefining the attributes and method for the child class")

class Battery:
    '''a simple attempt to model a battery for an electric car'''
    def __init__(self,battery_size = 40):
        '''initialize the battery attributes'''
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"this car has {self.battery_size}-kwh battery on it")
    ##lets define teh range of the battery 
    def get_range(self):
        '''print the statement about the range of this battery'''
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"this car can go about {range} miles on full charge")

class ElectricCar(Car):
    '''represents the aspects of the car, specifice to electriv vehicles'''
    def __init__(self,make,model,year):
        '''initialize attributes of the oarent class '''
        super().__init__(make,model,year) ##initialize the attributes from the parent class 
        self.battery = Battery() #now we can access the methods of the battery class from this class 
my_leaf = ElectricCar('leaf','nissan',2025)
my_leaf.get_descriptive_name()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()


##9.6
class Resturant:
    def __init__ (self,name,cuisine):
        self.name = name 
        self.cuisine = cuisine 
        self.order_record = 0 
    def resturant_desctiption(self): 
        print(f"the name of the resturant is {self.name} and it serves {self.cuisine}")
    def update_order(self,number):
        if self.order_record < number: 
            self.order_record = number
        else: 
            print("you cant decrease the number of order served")
    def show_order_record(self):
        print(f"the number of order served is {self.order_record}")
class IceCreamStand(Resturant): 
    def __init__(self,name,cuisine='icecream',*flavours):
        super().__init__(name,cuisine)
        self.flavours = flavours
    def show_flavours(self):
        print("they serves these flavours: ")
        for flavour in self.flavours:
            print(flavour)
ic1 = IceCreamStand('The pepe','icecreams','venella','chocolate','mango')
ic1.resturant_desctiption()
ic1.show_flavours()
ic1.update_order(100)

            
##9.7 admin 
class User: 
    def __init__(self,first_name,last_name):
        self.first_name = first_name 
        self.last_name = last_name 
        self.login_attempts = 0 
    def greet_users(self): 
        print(f"Hi Mr/Mrs {self.last_name}")
    def see_login_attempts(self):
        print(f"you have performed total {self.login_attempts} login attempts")
    def update_login_attempts(self,number): 
        if number < self.login_attempts: 
            print("sorry the number of login attempts cant be reversed")
        else: 
            self.login_attempts = number 
    def increment_login(self,number): 
        self.login_attempts += number 
class Admin(User):
    def __init__(self,first_name,last_name,*privilages): 
        super().__init__(first_name,last_name)
        self.privilages = privilages
    def show_privilages(self): 
        for privilage in self.privilages:
            print(privilage)
Admin1 = Admin('Prakash','chandra','Can add user','can add post','can deleter user')
Admin1.greet_users()
Admin1.update_login_attempts(10)
Admin1.update_login_attempts(2)
Admin1.increment_login(2)
Admin1.see_login_attempts()
Admin1.show_privilages()


##9.8 privilages 
class User: 
    def __init__(self,first_name,last_name):
        self.first_name = first_name 
        self.last_name = last_name 
        self.login_attempts = 0 
    def greet_users(self): 
        print(f"Hi Mr/Mrs {self.last_name}")
    def see_login_attempts(self):
        print(f"you have performed total {self.login_attempts} login attempts")
    def update_login_attempts(self,number): 
        if number < self.login_attempts: 
            print("sorry the number of login attempts cant be reversed")
        else: 
            self.login_attempts = number 
    def increment_login(self,number): 
        self.login_attempts += number

class Privilage: 
    def __init__(self): 
        self.privilages = ['can add users','can create post','can delete post']
    def show_privilages(self):
        print("here are the privilages that the admin can  have") 
        for privilage in self.privilages: 
            print(privilage)
class Admin(User): 
    def __init__(self,first_name,last_name): 
        super().__init__(first_name,last_name)
        self.privilage = Privilage()
Admin1 = Admin('Prakash','chandra')
Admin1.greet_users()
Admin1.update_login_attempts(40)
Admin1.increment_login(2)
Admin1.see_login_attempts()
Admin1.privilage.show_privilages()






