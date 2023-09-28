# 1. What is the difference between 
# a parameter and an argument in a python function

"a parameter is a palce holder and arguments are like data or evidence"

# 2. In your own words, describe what 
# a conditional statement (if/else) is 

"its like is like a true or false kinda thing, like if the password is AkeelAli(true) it will let u in"
" and else is if u put in anything BUT the password(false) it wont let u in"

# 3. write a simple conditional state using a comparision operator(greater than, less than, etc. )

money_in_acc = 100.00
cost_of_hoodie = 89.99

if money_in_acc > cost_of_hoodie:
    print("congrats you bought the hoodie")
else:
    print("sorry, get ya money up :/")

# 4. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false. 
# your function should have a line of code that asks the user if there is food in the refridgerator.
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 

def food_in_fridge():
    food_in_fridge = False
    
if food_in_fridge == True:
    print("time too cook")
else:
    print("time to shop")

# 5. Create a function that checks the inventory of cereal for a store. 
# your function should have a parameter that accepts an integer. In your function
# use a conditional statement to determine if you need to order more cereal.
# If there is more than 10 boxes, print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".

def cereal_inventory(cereal):
    current_cereal_inventory=10

    if cereal >= current_cereal_inventory:
        print ("inventory full")
    else:
        print ("we need to order more cereal boxes")

cereal_inventory(11)