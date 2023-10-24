# 1. In your own words, describe what a for loop is?

" its a loop that goes through lists and prints it repeatingly"

" a loop thay repeats a block of code a specific amout of times."
# 2. What is the difference between a FOR loop and a WHILE loop?
# Provide two (2) examples of each. 

"while loops execute a set of statements as long as a condition is true"
"for loops execute a set of statements once for each item in a list, tuple, set etc."

"WHILE loops"

i = 1
while i < 6:
  print(i)
  i += 1

'For loops'

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)



# 3. Create a FOR loop that will go through a list of names 
# and print all the names that start with the letter "R".


names=['Michael','Rebecca','William','Kareem','Robert','Rose','Jason']

for firstLetter in names:
  if firstLetter[0] == 'R':
    print(firstLetter)