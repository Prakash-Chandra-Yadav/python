##lets say you want to see all the names in the list or perform the repeatitive task on the list, in that you may want to use the loop on the list 
magicians = ["alice","david","carolina"]
for magician in magicians:
    print(magician)

##doing more work withing a loop 
for magician in magicians:
    print(f"Hello! Mr/Mrs.{magician} you performed a great trick!!")

##what if you want to display something after the end of the loop simple display message in the end 
for magician in magicians:
    print(f"Hello! Mr/Mrs.{magician} you performed a great trick!!")
print("Thankyou everyone that was the great magic show")

##Try It yourself 
#4.1
pizzas = ["cheese","mushroom","peperoni"]
for pizza in pizzas:
    print(f"i like {pizza} pizza")
print("i like pizza very much")

#making numerical List 
#using range function 
for i in range(1,5):
    print(i)
print(range(1,9))

numbers = list(range(1,8))
print(numbers)

#what if we want to print the number in the certain range in the range of 2, last number is the step size
even_numbers = list(range(2,11,2))
print(even_numbers)

#what if we want to perform something with the number in that range and then append in the empty list 
squares = []
for i in range(1,11):
    square = i**2
    squares.append(square)
print(squares)

#what if we want to add the cube of the number from 1,11 in difference of 2
cubes = []
for i in range(1,11,2):
    cube = i**3
    cubes.append(cube)
print(cubes)

##what if list contains the numbes as an item and you want to perform some operation that 
##like get the minimun value in the list,. or maximum or the sum 
digits = [1,2,3,4,5,6,7,8,9,10]
print(min(digits))
print(max(digits))
print(sum(digits))

#now this is the list comprehension we can writw thw for loop in the list and it works as the previous for loop code 
squares = [value**2 for value in range(1,11)]
print(squares)

#try it yourself 
number1 = list(range(1,21))
print(number1)

#4.3
number2 = []
for i in range(1,21):
    number2.append(i)
print(number2)

# #4.4 
# millions = list(range(1,1000001))
# for number in millions:
#     print(number)
# print("1 millions numbers printed successfully")

# #4.5
# print(min(millions))
# print(max(millions))
# print(sum(millions))

#4.6 
odd_numbers = list(range(1,21,2))
for digit in odd_numbers:
    print(digit)
#4.6 
print("now table of 3")
table_of_three = list(range(3,31,3))
for number in table_of_three:
    print(number)

#4.9 
cubes = [value**3 for value in range(1,11)]
print(cubes)

#working with parts of lists 
##what if you want to work with certain part of the list 
players = ["martina","charles","michael","florence","eli"]
print(players)
print(players[0:3]) #note that the last element in the slide is not incuded 

print(players[1:4])

#what if you want to select the item from starting position specified but that last position 
print(players[2:])

#simillarly if you dont provide the starting index python will start from the begining of the list 
print(players[:3]) #last selected position is ommited 

##simillarly if you want to  print the last 3 players names
print(players[-3:])

##if you inclue the 3rd value it will act same as the range method in which the 3rd value was used for skipping the defined numbers of items 

#looping through the slides 
print("here are the first 3 players of my team: ")
for player in players[:3]:
    print(player.title())
##Try it yourself 
friend_names = ["ram","shyam","ghanshyam","guddhu","banti","chintu"]
##print the messahe to the first three friends 
for name in friend_names[0:3]:
    print(f"hello {name}")

for name in friend_names[3:]:
    print(f"hello {name}")

for name in friend_names[-3:]:
    print(f"-hello {name}")
