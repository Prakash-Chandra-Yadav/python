def greet_user():
    """display a sample greetings"""
    print("hello!")
greet_user()

##passing an iformation to a fucntion 
def greet_user(username):
    '''display a simple greetings'''
    print(f"hello Mr/Mrs {username.title()}")
greet_user('Prakash')

##positional arguments (in this type of arguments the position  matters)
def describe_pet(animal_type, pet_name):
    '''Display information about a pet'''
    print(f"i have {animal_type}")
    print(f"my {animal_type.title()} name is {pet_name.title()}")
describe_pet('hamster','harry')


#youi can assisicate the argumemt keyword withthe argument value to avoid any confusione or the order error 
#and while using the keyword argyuments be sure to use the exact paramater name you have declared in the function
describe_pet( pet_name='billa',animal_type='dog')

#defauld value, you can declare the default value of the parameter in the function as well so if user will not provide any arguments it will be consideres as the default value 
def describe(pet_type,pet_name='nothing'):
    print(f"i have a {pet_type.title()}")
    print(f"the name of my {pet_type.title()} is {pet_name.title()}")
describe(pet_type='cat')

##Equivalent Function call 
##this means that the finction that we declared above  can be called in the several ways 
#these two will have teh same output
describe('dog')
describe(pet_type='dog')

#all these three will have the same output
describe('dog','dogesh')
describe(pet_type='dog',pet_name='dogesh')
describe(pet_name = 'dogesh', pet_type = 'dog')

print("\n---------------next topics--------------")


##return values 
def get_formatted_name(first_name, last_name):
    '''return the full name neatly formatted'''
    full_name = f"{first_name} {last_name}"
    return full_name 
your_name = get_formatted_name('prakash','chandra')
print(your_name)

def get_formatted_name(first_name, last_name, middle_name=''):
    '''return a full name neatly formatted'''
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else: 
        full_name = f"{first_name.title()} {last_name.title()} "
    return full_name 
name1 = get_formatted_name('Prakash','Yadav')
name2 = get_formatted_name('Prakash','Chandra','Yadav')
print(name1)
print(name2)

print("\n----------New topic form here Returning as Dictionary----------------")
def build_person(first_name, last_name):
    '''return a dictionary of information about a person'''
    person = {'first':first_name, 'last':last_name}
    return person 
person = build_person('Prakash','chandra')
print(person)

##now lets add the persons name as well
def build_person(first_name, last_name, age= None):
    '''return a dictionary of information about a person'''
    person = {'first':first_name, 'last':last_name}
    if age: 
        person['age'] = age
    return person 
person1 = build_person('Prakash','chandra')
print(person1)
person1 = build_person('Prakash','chandra',25)
print(person1)

##using function with a while loop 
##lets greet the user unitl he quits 
def get_formatted_name(first_name,last_name,middle_name=''):
    '''greets the user with the full name'''
    if middle_name:
        full_name = f"hi {first_name.title()} {middle_name.title()} {last_name.title()}"
    else: 
        full_name = f"hi {first_name.title()} {last_name.title()}"
    return full_name 
while True: 
    print("please enter quit to stop")
    f_name = input("first name: ")
    if f_name == 'quit':
        break 
    m_name = input("middle name: ")
    if m_name == 'quit':
        break
    l_name = input("last name: ")
    if l_name == 'quit':
        break 
    greet = get_formatted_name(f_name,l_name,m_name)
    print(greet)

print("\n--------next topic from here (passing a list )-----------")
def greet_the_user(users):
    for user in users: 
        print(f"hello! {user.title()} nice to meet you")
users = ['prakash','chandra','yadav']
greet_the_user(users)

#lest work on modifyiomng the list 
register  = ['prakash','chandar','yadav']
registered =[]

def show_registered_user(users): 
    for user in users: 
        print(f"{user} is registered already!!")
def register_the_user(register,registered):
    while register: 
        current_register = register.pop()
        print(f"registering {current_register} .....")
        registered.append(current_register)
    print("finished registering all the users")
    show_registered_user(registered)
register_the_user(register,registered)

##nwo let say we dont want to modify the original register list 
##instad of working on the original list we can work on the copy



    