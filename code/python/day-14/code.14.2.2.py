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

def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left), height(node.right)) + 1
    
                    

rootNode= int(input('Enter the value of the root node in Tree 1:'))            
root=node(rootNode)

while True:
    continuestring=str(input('Press y to continue : '))
    if continuestring is 'y':
        inputNumber=int(input('Enter the value into the Tree 2 :'))   
        root.insert(inputNumber)
    else:
        break
    
print('The height of the Binary Tree is :',height(root))

