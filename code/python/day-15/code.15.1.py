string = str(input('Enter the string :'))

def occurenceString(string):
    dic ={}
    for n in string:
        keys = dic.keys()
        if n in keys:
            dic[n] +=1
        else:
            dic[n]=1

    print(dic)
occurenceString(string)

            
        
                
