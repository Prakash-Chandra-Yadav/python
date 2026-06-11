from pathlib import Path 
import json 

def get_stored_name(path):
    '''get the stored user name if avilable'''
    if path.exists():
        content = path.read_text()
        username = json.loads(content)
        return username 
    else: 
        return None
def get_new_username(path):
    '''prompt for the new user name'''
    username = input("please enter your name: ")
    content = json.dumps(username)
    path.write_text(content) 
    return username
def greet_user():
    '''greet the user by their name'''
    path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\exceptions\usernames.json')
    username = get_stored_name(path)
    if username:
        print(f"hi {username} glad to see you again")
    else: 
        username = get_new_username(path)
        print(f"I will remember you {username}")
greet_user()