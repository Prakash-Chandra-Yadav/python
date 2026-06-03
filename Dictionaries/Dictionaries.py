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

##looping through all values in dictionaries

