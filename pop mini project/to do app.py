from colorama import Fore, init, Style
init()


#create the list taht will store the information about the user
users = []
#create the dictionary that stores the details about the users 
user_info = {}

##we have to use the dictionary inside the dictionary to store the store ths users information
def create_account():
    name = input(Fore.WHITE + "please enter your  name: " + Style.RESET_ALL)
    while True:
        user_name = input(Fore.WHITE + "please enter the user name: " + Style.RESET_ALL).lower().strip()
        if user_name not in users: 
            password = input(Fore.WHITE + "please enter the password: " + Style.RESET_ALL)

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
                    confirm_password = input(Fore.WHITE + "please confirm the password: " + Style.RESET_ALL)
                    if confirm_password == password: 
                        print(Fore.GREEN + f"account created successfully ! welcome {user_name}" + Style.RESET_ALL)
                        user_info[user_name] = {'name':name,'password':confirm_password}
                        users.append(user_name)
                        validate = False
                    else: 
                        print(Fore.RED + "password didnt match please try again!!" + Style.RESET_ALL)
                else: 
                    print(Fore.RED + "Passwor should have the combination of uppercase lower case number and special characetrs" + Style.RESET_ALL)
                    break
            break  
        else:
            print(Fore.GREEN + "user already exists" + Style.RESET_ALL)

##now create the function for login 
def login():
    while True:
        user_ID = input(Fore.WHITE + "please enter the user_name: " + Style.RESET_ALL).lower().strip()
        for name in user_info.keys():
            if name == user_ID:
                passwd = input(Fore.WHITE + "Please Enter the password: " + Style.RESET_ALL)
                for info in user_info[name]:
                    if user_info[name]['password'] == passwd:
                        print(Fore.GREEN + f"welcome! {name}" + Style.RESET_ALL) 
                        dashboard(name) 
                        return 
                    else: 
                        print(Fore.RED + f"wrong password" + Style.RESET_ALL)
            else:
                print(Fore.RED + "user name not found!! " + Style.RESET_ALL)

##now create the dashboard that will be shown to the user where he can create he to do and see his informations 
def dashboard(user_Id):
    print(Fore.GREEN + f"\nWelcome to the dashboard Mr/Mrs {user_Id}" + Style.RESET_ALL)
    while True:
        print(Fore.YELLOW + "\n---------------DASHBOARD------------------" + Style.RESET_ALL)
        print("1.Create the to do task")
        print("2.See the list of your to do task")
        print("3.delete the to do task")
        print("\n4.Logout")

        choice = input(Fore.WHITE + "Please selecte an option from above: " + Style.RESET_ALL)
        match choice:
            case '1':
                create_task(user_Id)
            case '2':
                see_task(user_Id)
            case '3':
                delete_task(user_Id)
            case '4':
                print(Fore.GREEN + "see you soon! be productive!!" + Style.RESET_ALL)
                break 

#let the user create the task
def create_task(user_ID):
    print(Fore.GREEN + "---please enter the tasks------" + Style.RESET_ALL)
    while True: 
        task_list = []
        task = input(Fore.WHITE + "please enter the task: " + Style.RESET_ALL)
        if task == 'done'or 'Done'or 'DONE':
            see_task(user_ID)
            break 
        else: 
            task_list.append(task)
            user_info[user_ID]['tasks'] = task_list
            print(Fore.GREEN + "saved the task that you just entered, enter 'done' to quit" + Style.RESET_ALL)

##let the user see the task 
def see_task(user_ID):
    print(Fore.GREEN + "\n---------LISTS OF YOUR TASK--------" + Style.RESET_ALL)
    if 'tasks'in user_info[user_ID]:
        for task in user_info[user_ID]['tasks']:
            print(task)
    else: 
        print(Fore.GREEN + "hmm.. seems like you have  no tasks today" + Style.RESET_ALL)

##let the user delete the task 
def delete_task(user_ID):
    print(Fore.GREEN + "\n---------LISTS OF YOUR TASK--------" + Style.RESET_ALL)
    if 'tasks'in user_info[user_ID]:
        for task in user_info[user_ID]['tasks']:
            print(task)
        print("copy and paste the task you wan to remove")
        selected_task = input(Fore.WHITE + "paste the task here: " + Style.RESET_ALL)
        user_info[user_ID]['tasks'].remove(selected_task)
    else:
        print(Fore.RED + "your task list is empty" + Style.RESET_ALL)


def main():
    print("\n------welcome to the to do app---------" )
    while True: 
        print("\n1. CREATE AN ACCOUNT")
        print("\n2. LOGIN")

        option = input(Fore.WHITE + "please select the option: " + Style.RESET_ALL)
        match option: 
            case '1':
                create_account()
            case '2':
                login()
                break 
            case '':
                print("please selecte the valid option")

main()