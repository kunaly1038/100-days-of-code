def fun():
    arr = []
    subarray=[]
    key = 0
    x = int(input('How many numbers you want to enter in Arrya :'))
    for i in range(x):
        xy = int(input('Enter the number into the arrya :'))
        arr.append(xy)

    print(arr)
    for i in range(len(arr)):
        key = arr[i]
        j=i-1
        while (j>=0 and  key<arr[j]):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key
    print(arr)


    
    subarray.append(arr[0])
    for i in range(len(arr)-1):
        key=arr[i+1]-arr[i]
        if(key == 1):
            subarray.append(arr[i+1])
        else:
            break
   

    print(subarray)

fun()
