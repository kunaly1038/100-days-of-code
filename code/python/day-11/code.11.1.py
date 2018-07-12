def missing():
    
    array=[]
    x = int(input('How many Elements you want in Array :'))
    
    for i in range(x):
        y = int(input('Enter the element :'))
        array.append(y)
    xy = array[0]
    for i in range(1,len(array)):
        xy+=1
        if(xy==array[i]):
            pass
        else:
            print(xy)
            break
missing()
