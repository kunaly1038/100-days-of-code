class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            if self.data <data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data= data
    def printTree(self):
        if self.left:
            self.left.printTree()

        print(self.data)

        if self.right:
            self.right.printTree()

def identicalTree(a, b):
     
    
    if a is None and b is None:
        return True
 
    if a is not None and b is not None:
        return ((a.data == b.data) and
                identicalTree(a.left, b.left)and
                identicalTree(a.right, b.right))
     
    return False
 
    
                    

rootNode= int(input('Enter the value of the root node in Tree 1:'))            
root=node(rootNode)

while True:
    continuestring=str(input('Press y to continue : '))
    if continuestring is 'y':
        inputNumber=int(input('Enter the value into the Tree 2 :'))   
        root.insert(inputNumber)
    else:
        break


rootNode2= int(input('Enter the value of the root node in Tree 2:'))            
root2=node(rootNode2)

while True:
    continuestring2=str(input('Press y to continue : '))
    if continuestring2 is 'y':
        inputNumber2=int(input('Enter the value into the Tree 2 :'))         
        root2.insert(inputNumber2)
    else:
        break
print(identicalTree(root,root2))

