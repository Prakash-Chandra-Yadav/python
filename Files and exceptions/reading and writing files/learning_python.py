##this is the exercise 
#10.1 
#learning the python 
from pathlib import Path 
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\things_i_learned.txt')
content = path.read_text().rstrip()
lines = content.splitlines()
for line in lines: 
    print(line)

print("\n---------dircetly printed the content from here-----------\n")

print(content)

print("\n---------Replacing the words in the lines of the text--------\n")
for line in lines: 
    modified = line.replace('python','c')
    print(modified)

print("--------simpler code --------\n")
for line in content.splitlines():
    print(line)