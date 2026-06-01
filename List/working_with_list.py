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
