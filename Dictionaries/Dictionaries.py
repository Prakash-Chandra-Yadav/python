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