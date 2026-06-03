alien_0 = {'color':'green','points':5}
print(alien_0['color']) #w have provided the key here so it will print the value 

#adding new key value pair in a dictionaries 
print(alien_0)
alien_0['x_positions'] = 0
alien_0['y_positions'] = 25
print(alien_0)

##starting with the empty dictionaries 
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5 
print(alien_1) 

##lets change the alien position according to its speed 
alien_2 = {'x_position':0, 'y_position':25, 'speed':'speed'}
#mode the alien to the right 
#determine how far the alien can move according to its current speed 
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else: 
    #this must be faster alien 
    x_increment = 3
#now the new position of the alien is olde position + increment 
alien_2['x_position'] = alien_2['x_position'] + x_increment
print(f"new position of the alien is {alien_2['x_position']}")

##removing the key value pairs from the dictationaries 
alien_3 = {'color':'green','points':5}
del alien_3['color']
print(alien_3)

#using get() to access the variable 
##sometimes if the key doesnt exists in the dictionary it will produce the error if we try toa accedd the key directlt so instead we can use the get() method 
alien_3 = {'color':'green','points':8,'x_position':2,}
speed_value = alien_3.get('speed', 'there is now key as such ')
print(speed_value)

#looping through the dictationaries 
user_0 = {'username':'efermi',
          'first':'enrico',
          'last':'fermi',}
for key,value in user_0.items():
    print(f"key: {key}")
    print(f"value: {value}")

##dictionaries  loopin through dictionaries using item()
favorite_language = {'jen':'python',
                     'sarah':'c',
                     'edward':'rust',
                     'phil':'python',}
for name, languages in favorite_language.items():
    print(f"{name.title()} likes {languages.title()}")


##what if only want to loop in the keys 
for key in favorite_language.keys():
    print(f"hi!! {key}")

##hwat if you want to loop on values 
for value in favorite_language.values():
    print(f"{value}")

#what if we want to check if certain keys exists in the dictionary 

print(favorite_language.keys())
if 'phil' in favorite_language.keys():
    print("thanks for answering phil")
if 'Prakash' not in favorite_language.keys():
    print("please answer the question Prakash")
if 'R' not in favorite_language.values():
    print("so R is not anyones favorite language")
#looping through the list in the particular order 
#what if we want to sort the persons name by the alphabetical order 
for name in sorted(favorite_language.keys()):
    print(f"{name.title()} your name comes in first place alphabetically")

for language in sorted(favorite_language.values()):
    print(f"{language.title()} comes first alphabetically")

for language in sorted(favorite_language.values(),reverse=True):
    print(f"{language.title()} comes first  reverse alphabetical order")

##NESTING 
##these are the alien details but how can we manage the fleet of aliens 
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':20}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

##a more realisting examples will be to create an emplty alien list and then add the aliens in it 

##make empty list for storing aliens 
aliens = []

##make 30 green aliens 
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

##show the firs 5 aliens 
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been cretaed 
print(f"the total number of aliens are {len(aliens)}")

##nwo change the coloe of first 3 aliens for yellow 
for alien in aliens[:3]:
    if alien['color'] =='green':
        alien['color'] ='yellow'
        alien['speed'] = 'medium'
        alien['points'] = 15
## now show the first 5 aliens and confirm if aliens have changed the color 
print("you can see that the first 3 aliens have changed the colors")
for alien in aliens[:5]:
    print(alien)

##so the example we have practiced above are the dictionary in the list 

##now what about list in a dictionary 

##store the information about the pizza being ordered 
pizza = {'crust':'thick',
         'toppings':['mushrooms','extra cheese'],
         }
##summarize the otder 
print(f"you have ordered the pizza with {pizza['crust']} crust \n with the following toppings")

#note that program will treat the pizza['toppins'] as the list becuase it is stored as a list inthe value 
for topping in pizza['toppings']: 
    print(f"{topping}")

##what if there are multiple keys as a value as a list 

favorite_language = {
    'jen': ['python','rust'],
    'sarah': ['c'],
    'edward' : ['rust','go'],
    'phil' : ['python', 'haskell']
}

##now print the person name with their favorite languages 
for name, languages in favorite_language.items():
    print(f"{name}'s favorite langauges are: ")
    for language in languages:
        print(f"{language.title()}")


##now dictionary in dictionary 
users = {
    'aeinstein': {'first':'albert',
                  'last':'einstein',
                  'location':'princeton',},
    'mcuire': {'first':'marie',
               'last':'curie',
               'location':'paris',},
}

##now print each users information 
for user, user_info in users.items():
    print(f"here are the details of: {user.title()}: ")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = f"{user_info['location'].title()}"
    print(f"fullname: {full_name.title()}")
    print(f"location: {location.title()}")

