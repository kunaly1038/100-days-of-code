def sorting_problem(x):
    for i in range(1,len(x)):
        key = x[i]
        j=i-1
        while(j>=0 and key<x[j]):
            x[j+1]=x[j]
            j-=1
        x[j+1]=key


x = [1, 0, 1, 1, 1, 0, 0, 1, 0]
sorting_problem(x)
print(x)
