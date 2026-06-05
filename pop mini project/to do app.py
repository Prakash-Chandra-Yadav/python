#create the list taht will store the information about the user
users = []
#create the dictionary that stores the details about the users 
user_info = {}
##we have to use the dictionary inside the dictionary to store the store ths users information
def create_account():
    name = input("please enter your  name: ")
    while True:
        user_name = input("please enter the user name: ")
        if user_name not in users: 
            password = input("please enter the password: ")
            has_lower = False 
            has_upper = False 
            has_number = False 
            has_special = False 
            special = ["!",'@',"#"]
            validate = True 
            while validate:
                for character in password: 
                    if character.isupper():
                        has_upper = True 
                    elif character.islower():
                        has_lower = True 
                    elif character.isdigit():
                        has_number = True
                    elif character in special:
                        has_special = True
                if has_upper and has_lower and has_number and has_special:
                    confirm_password = input("please confirm the password: ")
                    if confirm_password == password: 
                        print(f"account created successfully ! welcome {user_name}")
                        user_info[user_name] = {'name':name,'password':confirm_password}
                        validate = False
                    else: 
                        print("password didnt match please try again!!")
                else: 
                    print("Passwor should have the combination of uppercase lower case number and special characetrs")
                    break
            break  
        else:
            print("user already exists")
##now create the function for login 
def login():
    while True:
        user_ID = input("please enter the user_name: ")
        for name in user_info.keys():
            if name == user_ID:
                passwd = input("Please Enter the password: ")
                for info in user_info[name]:
                    if user_info[name]['password'] == passwd:
                        print(f"welcome! {name}")  
                        return 
                    else: 
                        print(f"wrong password")
            else:
                print("user name not found!! ")
##now create the dashboard that will be shown to the user where he can create he to do and see his informations 
def dashboard(user_Id):
    print(f"\nWelcome to the dashboard Mr/Mrs {user_Id}")
    while True:
        print(f"\n---------------DASHBOARD------------------")
        print("1.Create the to do task")
        print("2.See the list of your to do task")
        print("3.delete the to do task")
        print("Logout\n")

        choice = input("Please selecte an option from above")
        match choice:
            case '1':
                create_task()
            case '2':
                see_task()
            case '3':
                delete_task()
            case '4':
                print("see you soon! be productive!!")
                break 
#let the user create the task
def create_task(user_ID):
    print("---please enter the tasks------")
    while True: 
        task_list = []
        task = input("please enter the task: ")
        if task == 'done':
            see_task(user_ID)
            break 
        else: 
            task_list.append(task)
            user_info[user_ID]['tasks'] = task_list
            print("saved the task that you just entered")
##let the user see the task 
def see_task(user_ID):
    print("\n---------LISTS OF YOUR TASK--------")
    for task in user_info[user_ID][tasks]:
        print(tasks)

##let the user delete the task 
def delete_task(user_ID):
    print("\n---------LISTS OF YOUR TASK--------")
    for task in user_info[user_ID][tasks]:
        print(tasks)
    print("copy and paste the task you wan to remove")
    selected_task = input("paste the task here: ")
    user_info[user_ID][tasks].remove(delete_task)


def main():
    print("\n------welcome to the to do app---------")
    while True: 
        print("\n2. CREATE AN ACCOUNT")
        print("\n1. LOGIN")

        option = input("please select the option: ")
        match option: 
            case '1':
                create_account()
            case '2':
                login()
                break 
            
        

