def calculator():
    def addition():
        x=int(input('Enter the first number: '))
        y=int(input('Enter the second number: '))
        print(x+y)
    def substraction():
        x=int(input('Enter the first number: '))
        y=int(input('Enter the second number: '))
        print(x-y)
    def multiplication():
        x=int(input('Enter the first number: '))
        y=int(input('Enter the second number: '))
        print(x*y)
    def division():
        x=int(input('Enter the first number: '))
        y=int(input('Enter the second number: '))
        print(x/y)   
    def error():
        print('INVALID VALUES')
    calcdictionary={
        '+':addition,
        '-':substraction,
        '*':multiplication,
        '/':division
        }
    x=input('''Enter your choice:
                + : Addition
                - : Substraction
                * : Multplication
                / : Division...''')
    calcdictionary.get(x,error)()

while(True):
    user = str(input('Enter y for continue...'))
    check='y'
    if(user==check):
        calculator()
    else:
        break

        

