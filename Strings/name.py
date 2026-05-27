name = "ada lovelace"
print(name.title()) 

# ##print the name of the variable it should be in the lower case 
# variable = input("enetr the variable and i will convert into the correct format")
# print(variable.lower())

# ##fullname .py 
# first_name = "prakash"
# last_name = "chandra"
# full_name = f"{first_name} {last_name}"
# message = (f"hello!! {full_name.title()}")
# print(message)


# ##adding white spaces into the string 
# print("python")
# print("\tPython 'i have use the tab here'")
# print("some programming languages are:\nPython\nJava\nC

# ##removing the white spaces (what if the user add the extras spaces i the crediantials)
 ##problem
name = "Prakash"
username = input("please! enter your user name: ")
if username == name: 
    print("wellcome!!")
else: 
    print("sorry the crediantials is wrong!!") #user will get the error if he will put the extra spaces in his name 

print("this is the solution we can strip out the spaces after or before the name")

if (username.lstrip() == name  or username.rstrip() == name): 
    print("wellcome!!")
else: 
    print("sorry the crediantials is wrong!!")