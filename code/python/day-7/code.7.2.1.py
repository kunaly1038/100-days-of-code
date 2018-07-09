def fun():
    arr = []
    x = int(input('How many numbers you want to enter in Array :'))
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
