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
                    


            
        

