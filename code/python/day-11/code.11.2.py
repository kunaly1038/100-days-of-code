def decimal(x):
    if(x>1):
        decimal(x//2)
    
    print((x%2))
x = int(input('Enter the number :'))
decimal(x)
