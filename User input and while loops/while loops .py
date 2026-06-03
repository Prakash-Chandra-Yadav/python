##introducing the while loops 
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1

##letting the user to choose when to quit 
prompt = "\nTell me something, and all I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program: "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

#using flag to control the loop 
prompt = "\nEnter something and i will repeat back to you: "
prompt += "\nPlease enter 'quit' to exit from the loop "
flag = True 
while flag:
    message = input(prompt)
    if message == "quit":
        print("surething closing the loop")
        flag = False 
    else: 
        print(message)

##using break to exit the loop 
print("\n please ennter the city name you want to suggest me to visit: ")
print("\nEnter quit to exit the loop: ")
while True: 
    city = input("enter the city name: ")
    if city == 'quit':
        break 
    else: 
        print(f"i would love to go to {city.title()}")
#using continue in a loop 
current_number = 0 
while current_number < 10: 
    current_number += 1
    if current_number % 2 == 0:
        continue 
    else:
        print(current_number)

#using while loops in lists and dictionaries 

##start with the user that need to be verified 
#and empty list to hold the unconfirmed user 
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"please wait we are verifying {current_user.title()}")
    confirmed_users.append(current_user)
for user in confirmed_users: 
    print(f"{user.title()} has been verified")

#remove all of instances specific values from a list 
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'dog' in pets: 
    pets.remove('dog')
print(pets)

## filling a dictationary with a user input 
responses = {}
##set the fplag to indicate that the polling is active
polling_active = True 
while polling_active:
    name = input("enter your name: ")
    response = input("which mountain would ypu like to climb: ")
    #store the response in the dictionary 
    responses[name] = response 

    #find out if anyone else is going to take the poll 
    repeat = input("would you like to let another person respond? yes/no : ")
    if repeat == 'no':
        polling_active = False 
#show the result 
for name, response in responses.items():
    print(f"{name.title()} would like to climd {response.title()}")