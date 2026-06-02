requested_toppings = ["mushrooms","extra cheese"]
if "mushrooms" in requested_toppings:
    print("adding mushrooms")
if "peperoni" in requested_toppings: 
    print("adding peperoni")
if "extra cheese" in requested_toppings: 
    print("adding extra cheese")
print("\n finished making your pizza!!")

##try yourself 
#5.3
alien_color = "green"
if alien_color == "green":
    print("you have just earned 5 points")
else: 
    print("")
#5.4
alien_color = "green"
if alien_color == "green":
    print("you have just earned 5 points")
else: 
    print("you have earned 10 points")

#5.5
alien_color = "green"
if alien_color == "green":
    print("you have just earned 5 points")
if alien_color == "yellow":
    print("you have just earned 10 points")
if alien_color == "red":
    print("you have just earned 15 points")
else: 
    print("")

##using if statement in a list 
##using multiple lists 
available_toppings = ["mushrooms","olives","green papers","pepproni","pineapple","extra cheese"]
requested_toppings = ["mushrooms","french fries","extra cheese"]

for requested_topping in requested_toppings: 
    if requested_topping in available_toppings:
        print(f"adding {requested_topping} in your pizza!!")
    else: 
        print(f"sorry! we are out of {requested_topping}")
