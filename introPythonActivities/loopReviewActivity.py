#password thing
passcode = 1234
passcodeAteempt_count = 0

while passcodeAteempt_count < 4:
    passcodeAtempt = int(input('please enter password '))
    if passcodeAtempt != passcode:
        print('incoret password')
    else:
        print('correct')
        break
    passcodeAteempt_count +=1

