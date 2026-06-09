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

class Battery: 
    def __init__(self,battery_size=40):
        self.battery_size = battery_size
    def show_battery_capacity(self):
        print(f"this car has {self.battery_size}-kwh battery in it")
    def update_battery(self,number):
        if self.battery_size == number:
            print("you already have a same capacity battery")
        elif number == 65: 
            self.battery_size = 65
        elif number == 40: 
            self.battery_size = 40
        else: 
            print("sorry the car is only compatible with 40 or 65 kwh battery ")
    def get_range(self): 
        if self.battery_size == 40: 
            range =150 
        elif self.battery_size == 65:
            range = 225
        print(f"the car can go upto {range} miles on single charge")

class ElectricCar(Car):
    '''represents the aspects of the car, specifice to electriv vehicles'''
    def __init__(self,make,model,year):
        '''initialize attributes of the oarent class '''
        super().__init__(make,model,year) ##initialize the attributes from the parent class 
        self.battery = Battery() #now we can access the methods of the battery class from this class
    def fill_gas_tank(self):
        print("Sorry this is an electric car") 