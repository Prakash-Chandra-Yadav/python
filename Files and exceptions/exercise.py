##write the name of the person
from pathlib import Path
path = Path(r'C:\Users\Envay\Desktop\python\Files and exceptions\text_book.txt')

content = ''
while True:
    text = input("please enter the text you want to save in the txt file: ")
    if text != 'q':
        content += f'\n{text}'
    else: 
        print("thanks saving your response...")
        break
path.write_text(content)
print("respose saved")

read_lines = path.read_text().splitlines()
for line in read_lines:
    print(line)