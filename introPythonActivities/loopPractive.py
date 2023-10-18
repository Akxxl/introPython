# while
# loops are a function that use the while keyword
# we need to give it instructions, like any other function
# keeps a program running so long as its true

i=0
while i <5:
    print('we are learning abt loops')
    i+=1
print('out loop is done')
#----------------------------------------------------------------------------------------------------

# break stops a loop from repeating its selp
def breakEx():
    u=0
    while u <100:
        print('we are learning abt loops')
        u+=1
        if u == 5:
            break

#reakEx()
#continue skips the condition specified in your program

def continueEx():
    p=0
    while p <20:
        p+=1
        if p != 5:
            print('skip' + str(i))
            continue
        print(p)
continueEx()
