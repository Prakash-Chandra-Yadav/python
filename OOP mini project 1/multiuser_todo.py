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

        user_info[self.name]['address'] = self.address
        user_info[self.name]['password'] = self.password
        user_info[self.name]['tasks'] = []
        content = json.dumps(user_info)
        path.write_text(content)
    def login(self):
        print("\n------ENTER YOUR LOGIN DETAILS-------\n")
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
            else:
                print("task not found!!")

        