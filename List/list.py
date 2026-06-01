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