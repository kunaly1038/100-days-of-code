def insertion_sort():
    x = []
    y = int(input('How many elements you want to enter the array :'))
    for i in range(y):
        z = int(input('Enter the number :'))
        x.append(z)
    for i in range(len(x)):
        key = x[i]
        j=i-1
        while(j>=0 and key<x[j]):
            x[j+1] = x[j]
            j-=1
        x[j+1]=key
    print(x)
        
insertion_sort()
