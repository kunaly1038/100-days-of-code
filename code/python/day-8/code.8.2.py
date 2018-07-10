x = int(input('Enter size of array :'))
arr = []
for i in range(x):
    y = int(input('Enter the value into the array :'))
    arr.append(y)
for i in range(len(arr)):
    min = i
    for j in range(i+1,len(arr)):
        if(arr[min]> arr[j]):
            min = j
    arr[i],arr[min]=arr[min],arr[i]

for i in range(1,len(arr)-1,2):
    arr[i],arr[i+1]=arr[i+1],arr[i]
    print(i)
print(arr)
    
