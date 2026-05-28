##how does the python sees the number in the program
print(2+3)
print(3-2)
print(3/2)
print(3**2)
print(10**6)

##by default python supports the order of operation mathematically, but if you want to change the order you can use the () parentheses 
print(2+3*2)
print((2+3)*2)


##how does python treat the floats 
##by default python calls any number with decimal point as the float 
print(0.1+0.1)
print(3*0.1)
##even if you divide the one integer by another integer you will get the float 
print(4/2)


##digits can be grouped using the underscores, it will not effectthe execution 
universe_age = 14_000_000_000
print(universe_age)
print("python ignores the underscores")


##multiple assignmnets 
##values can be assigne to the more than one variables in a single line of code 
x,y,z = 1,2,3
print(x,y,z)


