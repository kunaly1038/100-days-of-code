import random

x = 0
y = 0

def user_Sum_Difference():
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    print('User tell the differnce between the numbers :',x,'-',y,'???')
    a=int(input('Enter here :'))
    if(a == x-y):
        print('Your answer is Correct')
    else:
        print('Your answer is Wrong')
        print('Correct answer is : ', x - y)
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    print('')

    a = int(input('Enter Here :'))
    print('User tell the sum of the numbers :',x,'+',y,' ???')
    if(a == x+y):
        print('Your answer is Correct')
    else:
        print('Your anser is Wrong')
        print('Correct answer is : ',x+y)


while (True):
    user_Sum_Difference()
