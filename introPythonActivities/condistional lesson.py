#write a condistional statement for if the sun is out

sun_is_out = False

if sun_is_out == True:
    print("do not turn on street lamps")
else:
    print("turn on street lights")


#write a conditional statment for purchasing a phone

money_in_acc = 1000
price_of_phone = 700.00

if money_in_acc > price_of_phone:
    print("congrats, you got the new phone")
else:
    print("sorry, insufficient funds.")

# write a function that will accept a user's password. The password should be a string paramater.
# if the password matchs, ket the user in, if the passowrd does not match , return incorrect password

user_password = "akeelali"

def login_password():
    user_password = input("please enter a password")
    if user_password == "akeelali":
        print("welcome, you are logged in")
    else:
        print("sorry, incorrect password")

login_password()