class Employeee: 
    def __init__(self,first_name,last_name,annual_salary):
        '''set the default attributes'''
        self.first_name = first_name 
        self.last_name = last_name 
        self.annual_salary = annual_salary

    def give_raise(self,rise=5000):
        '''give the annual raise of 5000 by default but user can ovveride this value as well'''
        self.annual_salary += rise 
    def get_employee_details(self):
        print(f"name: {self.first_name.title()} {self.last_name.title()} \n Sallary:{self.annual_salary}")
        
