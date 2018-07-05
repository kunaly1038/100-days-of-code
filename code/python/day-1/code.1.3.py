def factorial(y):
    if y == 1:
        return 1
    else:
        return y*factorial(y-1)

x = int(input('Enter the number:'))
xy=factorial(x)
print(xy)
