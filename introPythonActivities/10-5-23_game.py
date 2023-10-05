list_numbers = [1,2,3,4,5,6]

def multiplying():
      for n in list_numbers:
        print(n*3)

#multiplying()

#wut_kind = input('enter some info ')
def types():
    
    if wut_kind := int:
        print('your item is an int')
    else:
        print('your item is an str')

#types()

hot = 75.00
cold = 70.00
def temp():
    temp1 = float(input('what is the degrees? '))

    if  temp1 >= cold:
        print('it is cold outside')
        if temp1 >= cold or temp1 <= hot:
            print('the weather is perfect')
        else temp1 >= hot or temp1 <= cold:
    
    else:
         print('it is hot outside')

temp()
