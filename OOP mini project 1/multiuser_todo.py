from pathlib import Path 
import json 
#create the to do class ande everything will be inside that 
user_info = {}
class Todo:
    def __init__(self,name,address,password):
        self.name = name 
        self.address = address
        self.password = password
    def create_account(self):
        print("\n---------Please enter your details to create your account-------\n")
        path = Path(r'C:\Users\Envay\Desktop\python\OOP mini project 1\user_info.json')
        user_info[self.name] = {}
        user_info[self.name]['address'] = self.address
        user_info[self.name]['password'] = self.password
        user_info[self.name]['tasks'] = []
        content = json.dumps(user_info)
        path.write_text(content)
    def login(self):
        print("\n------ENTER YOUR LOGIN DETAILS-------\n")
        path = Path(r'C:\Users\Envay\Desktop\python\OOP mini project 1\user_info.json')
        global user_info
        content = path.read_text()
        user_info = json.loads(content)
        while True:
            name = input("please enter your name: ")
            if name in user_info.keys():
                password = input("please enter your password: ")
                if password == user_info[name]['password']:
                    self.dashboard()
                    break
                else: 
                    print("password didnt match please enter correct details!!")
            else:
                print("USER NOT FOUND!!")      
    def create_task(self):
        print("\n-----------Please enter the task you enter---------\n")
        while True:
            task = input("Please enter the task: ")
            if task != 'q':
                user_info[self.name]['tasks'].append(task)
                print("created the task")
            else:
                print("stopped saving tasks")
                break 
    def sow_task(self):
        print("\n--------here are your saved tasks-------\n")
        for task in user_info[self.name]['tasks'].values():
            print(task)
    def delete_task(self): 
        print("\n-------Please enter the task you want to delete-----\n")
        selected_task = input("enter the task to delete it: ")
        for task in user_info[self.name]['tasks']:
            if task == selected_task:
                user_info[self.name]['tasks'].remove(task)
                print("deleted the task!")
                break 
            else:
                print("task not found!!")
    def dashboard(self):
        print("\n------Welcome---------\n")
        print("------Please select the option from below---------")
        print("1>Create Task\n2>See Task\n3>Delete Task\n4>Logout")
        while True:
            choice = input("selecte the option from above: ")
            match choice:
                case '1':
                    self.create_task()
                case '2':
                    self.sow_task()
                case '3':
                    self.delete_task()
                case '4':
                    self.logout()
                    break 
def main():
    print("=======WELCOME TO THE TO DO APP=======")
    print("1>Create Account\n2.>Login")
    choice = input("plesase select the option: ")
    match choice: 
        case '1':
            name = input("Please enter your name: ")
            address = input("please enter your address: ")
            upper_case = False 
            Lower_case = False 
            Number_case = False 
            Special_case = False
            Special = ['@',"#",'!',"$"]
            while True: 
                password = input("please set the password: ")
                for letter in password:
                    if letter.isupper():
                        upper_case = True 
                    if letter.islower():
                            Lower_case = True
                    if letter.isdigit():
                        Number_case = True 
                    if letter in Special:
                        Special_case = True 
                if upper_case and Lower_case and Number_case and Special_case:
                    confirm_password = input("please confirm the password: ")
                    if password == confirm_password:
                        user1 = Todo(name,address,confirm_password)
                        user1.create_account()
                        print(f"your account has been created {name}")
                        user1.login()
                        return 
                    else: 
                        print("password didnt matched")
                else: 
                    print("password should have the combination of the number charcter and letters and atleast one upper case letter")
        case '2':
            user1.login()
main()
                



        