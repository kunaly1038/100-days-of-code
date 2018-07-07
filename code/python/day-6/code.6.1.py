list=[]
list2=[]
list3=[]


x = int(input('Enter the size of array :'))

for i in range(0,x):
    y = int(input('\nEnter the positive value into the array : '))
    list.insert(i,y)


for i in range(0,x):
    y =  int(input('\nEnter the negative number into the array : '))
    list2.insert(i,y)

print('\nYou entered elements in array 1st:',list)
print('\nYou entered elements in array 2nd:',list2)


for i in range(0,len(list)):
   x=0
   x=list[i]+list2[i]
   list3.append(x)
print('\nThe Sum of  sub array is :' ,list3)
print(list3)
