from pathlib import Path 
import json 
#define the list of the numbers
numbers = [1,24,5,76,23,90]
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\exceptions\numbers.json')
content = json.dumps(numbers)
path.write_text(content)

##now read the json file 
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)


print("\n-------another exercise from here-------\n")
username = input("whats the  name: ")
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\exceptions\username.json')
content = json.dumps(username)
path.write_text(content)

print(f"we will remember you next time you come back {username}")

#now greeet the user whos name has already been stored 
contents = path.read_text()
user1 = json.loads(contents)
print(user1)

#refactoring 
