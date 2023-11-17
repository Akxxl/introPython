
def calc():
    
    num1 = int(input('what is the first number you would like to use? '))
    num2 = int(input('what is the second number you would like to use? '))
    print('the types of math you can do is addition, subtraction, multiplication, division, or greater then or equal too ')
    print('type + for addition')
    print('type - for subtraction')
    print('type x for mutliplication')
    print('type / for division')
    print('type  <=> for greater than or equal too')
    wut = input('please enter the math you would like to use ------->  ')
    print('you answer to your math problem is listed below. ')
    
    if wut == '+':
        print(num1 + num2)
    
    elif wut == '-':
        print(num1 - num2)

    elif wut == '/':
        print(num1/num2)

    elif wut == 'x':
        print(num1*num2)

    elif wut == '<=>':
        if num1 > num2:
            print(str(num1) + ' is greater than ' + str(num2))

        elif num1 == num2:
            print(str(num1) + ' is equal too ' + str(num2))

        else:
            print(str(num1) + " is less than " + str(num2))

    else:
        print('error please retry and make sure u put in all the correct information')


    print('if you would like to do another calculation, run the program again. ')


calc()

