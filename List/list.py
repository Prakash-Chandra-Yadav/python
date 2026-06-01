##how does list looks like ?
bicycles = ["trek","cannodale","redline","specialized"]

##what if you want to print the name of your first bicycle
message = f"my first bicycle was {bicycles[0]}"
print(message)

##what if someone asks you what was your last bicycle 
next_message = f"my last bicycle was {bicycles[-1]}"
print(next_message)

##MODIFYING ADDING AND REMOVING ELEMENTS 

##modifying the value 
##what if you want to modify the name of you first bicycle as you remember it was diffrent than mentioned one 
bicycles[0] = "hero"
print(bicycles)

##Adding element inthe list 
##what if you want to add one more element 
bicycles.append("crossx")
print(bicycles)

##inserting new value ar any position in the list 

##what if you remember your 2nd bicycle was different than you mentioned and insted the 2nd bicycle was the 3rd one  
##well in that case we can use the insert() method, insert(position,'element')

bicycles.insert(1,'phoneix')
print(bicycles)

##removing an element from the list 

##well in that case if you know the position of and element you can ude the del statemebt 
del bicycles[0]
print(bicycles)

##using pop method, it removes the item from the end of the list 
popped_bicycles = bicycles.pop()
print(popped_bicycles)

##we can pop the items for any positions as well 

popped_bicycle = bicycles.pop(0)
print(popped_bicycle)

##what if we dont know the position of an item we want to removein that case we can use the remove fucntion 
motorcycles = ["hero","tvs","bajaj","yamaha","ninja"]
print(motorcycles)
motorcycles.remove('bajaj')
print(motorcycles)

##NOTe: remove method only removes the first occurance of the values 
##ty it yourself 

#3.4 
invitations = ["ram","shyam","ghanshyam","ramu","bibek", "abishek"]
print(f"{invitations[0]} is invited")
print(f"{invitations[1]} is invited")
print(f"{invitations[2]} is invited")
print(f"{invitations[3]} is invited")
print(f"{invitations[4]} is invited")
print(f"{invitations[5]} is invited")


#3.5 
invitations = ["ram","shyam","ghanshyam","ramu","bibek", "abishek"]
print(f"{invitations[0]} is invited")
print(f"{invitations[1]} is invited")
print(f"{invitations[2]} is invited")
print(f"{invitations[3]} is invited")
print(f"{invitations[4]} is invited")
print(f"{invitations[5]} is invited")

print(f"we have been informed that {invitations[4]} cant make it")

del invitations[4]
invitations.insert(4,'billu')

print(f"{invitations[0]} is invited")
print(f"{invitations[1]} is invited")
print(f"{invitations[2]} is invited")
print(f"{invitations[3]} is invited")
print(f"{invitations[4]} is invited")
print(f"{invitations[5]} is invited")

#3.6
del invitations[4]
invitations.insert(4,'billu')

print(f"{invitations[0]} is invited")
print(f"{invitations[1]} is invited")
print(f"{invitations[2]} is invited")
print(f"{invitations[3]} is invited")
print(f"{invitations[4]} is invited")
print(f"{invitations[5]} is invited/n")

print("so we have bigger table and we have plenty of spaces")

invitations.insert(0,'Prakash')
invitations.insert(2,'Raju')
invitations.append('Sita')
print(invitations)
print(f"{invitations[0]} is invited")
print(f"{invitations[1]} is invited")
print(f"{invitations[2]} is invited")
print(f"{invitations[3]} is invited")
print(f"{invitations[4]} is invited")
print(f"{invitations[5]} is invited")
print(f"{invitations[6]} is invited")
print(f"{invitations[7]} is invited")
print(f"{invitations[8]} is invited")

#3.7
print("sorry to inform but we only have space for two guests")
while len(invitations) >2:
    popped = invitations.pop()
    print(f"{popped} has been removed from the list")
   
for name in invitations:
    print(f"{name} is invited")

print(invitations)

del invitations[0]
del invitations[0]
print(invitations)
