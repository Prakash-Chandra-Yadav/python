user_info={}
user_list=[]

class Todo: 
    def __init__(self,user_name,password):
        self.user_name = user_name 
        self.password = password 
    def create_account(self):
        user_info['user_name'] = self.user_name 
        user_info['password'] = self.password
        user_info['tasks'] = []
        print(f"Welcome {self.user_name} your account has been created successfully")
    def create_task(self):
        while True: 
            task = input("please enter the task you want top save: ")
            if task == 'q':
                print("thanks!!! stay productive")
                break 
            else: 
                user_info['tasks'].append(task)
                print("task has been added")
    def login_account(self):
        while True: 
            user = input("please enter the name of the use: ")
            user_password = input("please enter your password: ")
            if user_password == user_info[user]['password']:
                print(f"-----------welcome-----{self.user_name}")
                self.dashboard()
                break 
            else: 
                print("please enter the correct password!!")
            
    def dashboard(self): 
        print("-----this is your dahsboard------")
        print("1.Create task")
        print("2.See_task")
        print("3.delete task")
        choose = input("please slecte the option: ")
        match choose: 
            case '1':
                self.create_task()
            case '2':
                self.see_task()
            case '3':
                self.delete_task()
        
    def see_task(self):
        i = 1
        if user_info['tasks']:
            print("you have no task to see")
        else:
            for task in user_info['tasks']:
                print(f"{i}-> {task}")
                i += 1
    def delete_task(self):
        print("select the task you want to delete")
        if user_info['tasks']:
            print("you have no task to delete")
        else: 
            select_task = input("please select the task you want to delete: ")
            user_info['tasks'].remove(select_task)  
            print("task has been deleted")
def main():
    print("------WELCOME TO THE TODO APP--------")
    print("1>Create account\n2>Login")
    while True:
        choice = input("please select the option from above: ")
        match choice: 
            case '1':
                name = input("please enter the user name: ")
                special_char = ['@',"!",'#','$',"%","&"]
                Special= False
                Number = False 
                Upper_case = False 
                Lower_case = False 

                while True: 
                    special_char = ['@',"!",'#','$',"%","&"]
                    Special= False
                    Number = False 
                    Upper_case = False 
                    Lower_case = False 
                    password_unconfirmed = input("please enter the password: ")
                    for char in password_unconfirmed: 
                        if char in special_char: 
                            Special = True 
                        elif char.isupper():
                            Upper_case = True 
                        elif char.islower():
                            Lower_case = True 
                        elif char.isdigit():
                            Number = True 
                    if Special and Upper_case and Lower_case and Number:
                        password_confirm = input("please confirm password: ")
                        if password_unconfirmed == password_confirm:
                                user1 = Todo(name,password_confirm)
                                break 
                        else: 
                            print("password didnt match with previous password")
                    else: 
                        print("please use the combination of NUmber, uppercase, lower case and special chars")
            case '2':
                user1.login_account()
                break 

main()
            


                        

                



