from pathlib import Path 
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

##relative and absolute file paths 
##the path we have useb above can be used as the absolute path
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\pi_digits.txt')
content = path.read_text()
lines = content.splitlines()
for line in lines:
    print(line)

##large files one million digits of pi
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\pi_digits.txt')
content = path.read_text()
lines = content.splitlines()
pi_string =''
for line in lines:
    pi_string += line.lstrip()
print(f"{pi_string[:52]}..")
print(len(pi_string))

##is you birthday containbed in the pi 
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\pi_digits.txt')
content = path.read_text()
lines = content.splitlines()
pi_string = ''
for line in lines:
    pi_string += line 
birthday = input("please enter your birthday: ")
if birthday in pi_string: 
    print("you birthday appears in pi")
else: 
   print("your birthday not appears in the pi")
