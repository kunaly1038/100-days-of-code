def selection_sort():
    x = []
    y = int(input('How many elements you want to enter the array :'))
    for i in range(y):
        z = int(input('Enter the number :'))
        x.append(z)
    for i in range(len(x)):
        min = i
        for j in range(i+1,len(x)):
            if(x[j]<x[min]):
                min = j
        x[i],x[min]=x[min],x[i]
    print(x)
        
selection_sort()
