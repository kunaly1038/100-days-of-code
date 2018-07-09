def fun():
    arr = []
    subarray=[]
    key = 0
    x = int(input('How many numbers you want to enter in Arrya :'))
    for i in range(x):
        xy = int(input('Enter the number into the arrya :'))
        arr.append(xy)
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(arr[j]==arr[i] and i!=j):
                duplicate=arr[j]
                break
            
    print(duplicate)

fun()
