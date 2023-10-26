# MID TERM QUIZ 


# RULES

# I. You may use google/ W3 schools to assist you with this exam

# II. Please make sure your answers/ responses are readable. You can write your written answers as comments or strings but 
# make sure that you are spacing your answers away from the questions. 

# III. You may use notes in your reposiory

# IV. You may not use any additional computing devices 
# (only one computer should be out).

# V. You may not use your phone during the quiz under any circumstances.
# If it is an emergency please request to be excused from the class. 

# VI. You may not have music or videos playing during the quiz
# under any circumstances. 

# VII. You may not use any LLM / AI applications under any circumstances. 
# Any one caught using  these applications will automatically fail the quiz.

# VIII. Save your work under the QUIZES folder

# _____________________________________________________________________


# Take your time, read the questions thoroughly, look for context clues

# The Code editor is your friend, run/ test your code. The computer will tell you if it's right or wrong.

# GOOD LUCK

# _____________________________________________________________________



# 1. Describe what a computer program is and what does it do. 

'a set of intructions a computer can execute'

# 2. Describe what complexitity and abstraction are, then provide an example
# of complexity in the real world and how we apply abstraction to that thing (you example must be original and cannot be an example
# used in our lecture slides ie car, grocery store, etc.). 

'complexity the measurement of the amount of resources it takes for a program to run'
'abstraction the process of simplifying complex programs.'

'an example of complexity is like a iPhone because it had all these sets of code in it but they did'
'abstraction so things like apps are just one little button'


# 3. What is Syntax in Python and why is it important to write proper syntax?

'the rules that determines how a python code will be written and interpreterd'

# 4. What is a function, and why do we wrap our code inside of functions?

'a funtion is a reuseable block of code, that we can use over and over again. we use Funtions because'
' it is a type of abtraction that will simplyfy the code that we had written '

# 5. Name and describe the three (3) naming conventions for variables in python? Then provide three (3) name rules for Python
# variables. 

'only can use letter a - z'
'only can use numbers 0-9'
'case sensitive(must use cases)'



# 6. What will be the output of the print functons when this code is ran, explain why
name = 'Bill'
student = name
name = 'Walter'
student= 'Richard'

print(name)
print(student)

'it will print walter and richard because it read code from top to bottom and the name and student'
'is closest to the print(name) and print(student) it will print out walter and richard'

# 7. Describe the difference between each of the following assignment operators:
# = 
# ==
# !=

'for = u can asign values to a varible like z = 9'
'for == it compairs variables'
'for != it means not equal to and u can use that for an if and else code'


# 8. What type of data can be stored in a python list?

'intergers float strings etc.'

# 9. Create a function that will take in a word provided by a user and then output that word back to the user but in reverse. 

def word():

    word1 = input('put in the word that you would like to revsere. ')

    print(word1[::-1])
word()


# 10. Create three (3) seperate functions that will do addition, subtraction, and multiplication respectively. 
# each of these functions should take two (2) arguments. When the user passes these arguments into the function, they will be
# calculated together and return the output in your terminal. 


def adding(x , z):
    print( x + z)
adding(10 , 4)


def subtracting(x,z):
    print(x - z)
subtracting(10,4)


def multiplying(x,z):
    print(x*z)

multiplying(10,4)

# 11. What is the difference between a function argument and a function parameter. 

'a function argument is like data/info'
'a function parameter is like a place holder for data'

# 12. You have been hired by a software company and your first assignment is to develop a password authenticator program. 
# the goal of your program is to check a user's password and make sure it meets the company's password requirements. 
# the company has provided you with the following requirements for the passcode program:
# a. the passcode must NOT contain any numbers
# b. the passcode must NOT contain any capital letters
# c. the passcode can NOT be any longer than five (5) characters
# d. the passcode can NOT shorter the three (3) characters
# e. the user should be able to enter their password and if it meets the requirements, should print a message saying that 
# their password was created successfully, and if it was not, should send back a message with one of the following issues. 



# 13. When you run your code and see typeError in your terminal, what does that typically mean and how would you try to solve
# the issue?

'typeError happens when u put in a command but it could not be preformed, probably u put in in wrong'

# 14. When you run your code and see indentError in your terminal, what does that typically mean and how would you try to solve 
# the issue?

'when u see indent eroor it mean u didnt indent something write and to fix it you just have to go'
'thought ur code and find the indetn error'


# 15. Create a while loop that check a user's password. If they enter the password correct, they will get a message saying 
# that the password was entered successfully. If they enter the password incorrectly, it will tell the user to try again. 
# The user should only have three (3) attempts to get the password correct. If they enter the password incorrect on the fourth 
# attempt, a message should appear telling them that have been locked out and need to talk to the administrator. 

passcode = 'Akeel1239$'
passcodeAteempt_count = 0

while passcodeAteempt_count < 3:
    passcodeAtempt = input('please enter password ')
    if passcodeAtempt != passcode:
        print('incoret password try again')
    else:
        print('Password entered sucsesfully')
        break

    passcodeAteempt_count +=1


# 16. Which item is at index 5
giftShopping=['xbox','sneakers','necklace','clothing','laptop','gift card']

'gift card is becuase the index count starts are 0 so xbox would be 0 and then gift card would be 5'
'and another was to show this is if we write print(giftShopping[5])'


# 17. Create a for loop that will print ONLY the even numbers within the range of the variable provided below.
# HINT: You will need to use the range() function. 
upToNumber = 30

things = range(2,31,2)
for thing in things:
    print(thing)


# 18. Create a function that uses a conditional statement that checks if a person qualifies for a raise on their salary. 
# The user should be able to enter their name, their salary (how much money they make in an entire year), and how long they have
# worked at the company. If the user has been working at the company longer than four (4) years, they will get a 15% raise. 
# Your program should be able to calculate what their salary is with the 15% increase. If the user qualifies, your program
# should return the a message congratulating the user by name, and telling them what their new salary is with the 15%
# increase (this must be the actual number). If they do not qualify inform the user that unfortunately they do not qualify. 


salery = 20.00
new_salery_raise = 1.15


def getting_raise():
    name1 = input('what is your name? ')
    how_long = int(input('how long have you been working at our company? '))

    if how_long > 3:
        print('congradulations'+ name1 +'your get a new raise')
        print('your new raise is below')
        print(salery*new_salery_raise)

    else:
        print('sorry you cant get a raise yet')

getting_raise()


# 19. Create a function that checks which value is greater than the other. Your function should take two (2) integer parameters. 
# and should evaluate which number is larger. Your function should then print the largest number. 



# 20. Create a while loop function that will add gift items to a list. Your function should ask the user to enter an item name. 
# The item name should then be added to a list variable called gift_bag. Your gift bag should have a limit of six (6) items. 
# Once your gift bag hits its limit of six (6) items your program should print a message saying 
# that the gift bag is full and print the list of items in the gift bag.   





