##import the related librarues and the class
from pathlib import Path 
import json 
# def get_favorite_number(path):
#     favorite_number = input("please enter your favorite number: ")
#     content = json.dumps(favorite_number)
#     path.write_text(content)
#     return favorite_number

# ##if the favourite number is already saved it will just dilplay the favorite number
# def show_favorite_number(path):
#     if path.exists():
#         content = path.read_text()
#         favorite_number = json.loads(content)
#         return favorite_number
# def main():
#     path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\exceptions\favorite.json')
#     favorite_number = show_favorite_number(path)
#     if favorite_number:
#         print(f"your favorite number is {favorite_number}")
#     else: 
#         favorite_number = get_favorite_number(path)
#         print(f"we will remember your favourire number is {favorite_number}")
# main()

##exercise 10.13
def get_user_info(path):
    user = {}
    name = input("please enter your name: ")
    address = input("please enter your address: ")
    contact = input("please enter your contact: ")
    user['name'] = name 
    user['address'] = address 
    user ['contact'] = contact 
    content = json.dumps(user)
    path.write_text(content)
    return user
def show_user_info(path):
    if path.exists():
        content = path.read_text()
        user = json.loads(content)
        return user 
    else: 
        return None
def main():
    path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\exceptions\user_info.json')
    user = show_user_info(path)
    if user: 
        print("\nHere are your details")
        for key,value in user.items():
            print(f"{key}:{value}")
    else: 
        user = get_user_info(path)
        print(f"we will remember your details {user['name']}")
main()





















path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\exceptions\favorite.json')

