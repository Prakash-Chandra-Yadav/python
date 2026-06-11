from pathlib import Path


try: 
    print(5/0)
except ZeroDivisionError:
    print("cant divide by zero")

print("\n------using an exception to prevent the crashes-----\n")

print("give me two numbers and i will divide them")
print("enter 'q' to quit")
while True: 
    first_number = input("please enter the first number: ")
    if first_number == 'q':
        break 
    second_number = input("please enter the second number: ")
    if second_number == 'q':
        break 
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("cant divide by zero")
    else: 
        print(answer)
    
print("\n-------handling the file not found exceptions-------\n")
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\exceptions\alice.txt')
try: 
    content = path.read_text()
except FileNotFoundError:
    print("sorry file not found")
else: 
    words = content.split()
    len_of_word = len(words)
    print(f"there are {len_of_word} words in the text file")

print("\n-------working with the multiple files-----/n")

def count_words(path):
    try: 
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("file not found")
    else:
        words = content.split()
        num_of_words = len(words)
        print(num_of_words)
filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
base_path = Path(r'C:/Users/Envay/Desktop/python/Files and exceptions/exceptions')
for filename in filenames: 
    path = base_path/filename
    count_words(path)

print("\n--------Failing silently-------\n")

def count_words(path):
    try: 
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = content.split()
        num_of_words = len(words)
        print(num_of_words)
filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
base_path = Path(r'C:/Users/Envay/Desktop/python/Files and exceptions/exceptions')
for filename in filenames: 
    path = base_path/filename
    count_words(path)