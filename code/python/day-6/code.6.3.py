def replacement(x):
    y=len(x)
    for i in range(0,y):
        if(x[i] == 0):
            key = x[i]
            j=i
            print(y)
            while(j<y-1):
                x[j]=x[j+1]
                j+=1
            x[y-1]=key     
    
    print(x)
x = [3, 0, 1, 0, 5, 9, 0, 6, 7]
replacement(x)












