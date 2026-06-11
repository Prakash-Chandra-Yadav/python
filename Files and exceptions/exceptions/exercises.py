from pathlib import Path 
# while True: 
#     first_number = input("enter the first number: ")
#     if first_number == 'q':
#         break 
#     second_number = input("please enter the second number: ")
#     if second_number == 'q':
#         break 
#     try: 
#         answer = int(first_number)+int(second_number)
#     except ValueError:
#         print("sorry!! enter the number please!!")
#     else: 
#         print(answer)


print("\n--------cats and dogs----------\n")
base_path = Path('C:/Users/Envay/Desktop/python/Files and exceptions/exceptions')
filenames = ['cats.txt','dogs.txt','rabbit.text']
for filename in filenames: 
    path = base_path/filename 
    try: 
        content = path.read_text()
    except FileNotFoundError:
        print("file not found !!")
    else: 
        print(content)

print("\n------------failing silently now----------------\n")
base_path = Path('C:/Users/Envay/Desktop/python/Files and exceptions/exceptions')
filenames = ['cats.txt','dogs.txt','rabbit.text']
for filename in filenames: 
    path = base_path/filename 
    try: 
        content = path.read_text()
    except FileNotFoundError:
        pass
    else: 
        print(content)

print("\n--------common words------------\n")

path = base_path/'test.txt'
try:
   content = path.read_text()
except FileNotFoundError:
    print("file not found")
else: 
    number = content.lower().count('python')
    print(f"the word 'python' repeats {number} times")

