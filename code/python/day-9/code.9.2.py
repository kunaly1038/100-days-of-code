def bubble_sort():
    x = []
    y = int(input('How many elements you want to enter the array :'))
    for i in range(y):
        z = int(input('Enter the number :'))
        x.append(z)
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if(x[j]>x[j+1]):
                x[j],x[j+1]=x[j+1],x[j]       
    print(x)
   
bubble_sort()
