from pathlib import Path 
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\programming.txt')
path.write_text('i love python.')

##writing miltiple lines 
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\programming.txt')
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love woring with data.\n"
path.write_text(contents)

lines = path.read_text().splitlines()
for line in lines: 
    print(line) 
print("\n-------Exercises from here--------------\n")
##try it yourself 
name = input("please enter the name: ")
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\guest.txt')
path.write_text(name)

content = path.read_text()
print(content)

##10.5 
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\guest_book.txt')
guest_list = []
content=''
while True: 
    name = input("please enter the name of the guest ")
    if name != 'q':
        guest_list.append(name)
        print("name has been recorded!!")
    else:
        for line in guest_list:
            content += f"{line}\n" 
        path.write_text(content)
        print("THANKS!! YOUR RESPONSE IS SAVED")
        break
book_content = path.read_text().splitlines()
for line in book_content:
    print(line)
        