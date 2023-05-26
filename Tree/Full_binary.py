#full binary 
class Node:
    def __init__ (self, val):
        self.value = val
        self.left =None
        self.right = None 

class FullBinaryTree:
    def __init__(self):
        self.root = None 
    #insert new node with values in tree
    def insert(self, value):
        newNode = Node(value)
        #agar node na hoi toh new root banao
        if not self.root:
            self.root =newNode 
        else: 
            currentNode = self.root
            while True:
                if not currentNode.left:
                    currentNode.left = newNode
                    break;
                elif not currentNode.right:
                    currentNode.right = newNode
                    break
                else:
                    currentNode = currentNode.left
                    
tree =FullBinaryTree()
tree.insert(1)                  
tree.insert(2)                  
tree.insert(3)                  
tree.insert(4)                  
tree.insert(5)                  
            
        
    
        