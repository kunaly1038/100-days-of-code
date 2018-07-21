class node:
    def __init__(self,data):
        
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
        if self.data:
            if self.data > data:
                if self.left is None:
                    self.left=node(data)
                else:
                    self.left.insert(data)
            elif self.data<data:
                if self.right is None:
                    self.right= node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

rootNode= int(input('Enter the value of the root node :'))            
root=node(rootNode)
while True:
    continuestring=str(input('Press y to continue : '))
    if continueString is 'y':
        print('Enter the number : ')
        inputNumber=int(input())
        root.insert(inputNumber)
    else:
        break
root.printTree()
        
