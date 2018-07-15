import random

def binary_search(array,l,r,x):
    if r>=l:
        mid = l + (r-l)//2
        if array[mid] is x:
            return mid
        elif array[mid]<x:
            return binary_search(array,mid+1,r,x)
        else:
            return binary_search(array,l,mid-1,x)
    else:
        return -1
        


array =[]
for i in range(0,100):
    array.append(random.randint(1,1000))
array.sort()
x = int(input('Enter the element you want to find into the array :'))
result=(binary_search(array,0,len(array)-1,x))
if result != -1:
    print('Your number is at :',result)
else:
    print('there is no such number :',x)
print(array)
