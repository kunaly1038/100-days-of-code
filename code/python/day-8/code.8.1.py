def fun():
    arr = []
    max1 = []
    x = int(input('How many numbers you want to enter in array :'))
    for i in range(x):
        xy = int(input('Enter the number into the array :'))
        arr.append(xy)
    max = 0   
    for i in range(len(arr)):       
        for j in range(len(arr)):
           if((arr[i] * arr[j]) > max and i!=j):
               max1.append(arr[i] * arr[j])
    for i in range(1,len(max1)):
        key =  max1[i]
        j=i-1
        while (j>=0 and key<max1[j]):
            max1[j+1]=max1[j]
            j-=1
        max1[j+1]=key
    
    max_find_pair=max1[len(max1)-1]
    for i in range(len(arr)):       
        for j in range(len(arr)):
           if((arr[i] * arr[j]) == max_find_pair and i!=j):
               print('{',arr[i],',',arr[j],'}')
               print('\n')
               
    
fun()
