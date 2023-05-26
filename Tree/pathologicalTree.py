#A Tree where every internal node has one child. Such trees are performance-wise same as linked list. A degenerate or pathological tree is a tree having a single child either left or right.

'''
        10
       /  \
      20
       \
        30
         \
          40  
'''

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class DegenerateTree:
    def __init__(self):
        self.nodes = []
    
    def insert(self, value):
        new_node = Node(value)
        #checking if node is empty it will append list
        if not self.nodes:
            self.node.append(new_node)
        else: 
            last_node = self.nodes[-1]
            last_node.next =new_node
            self.nodes.append(new_node)

if __name__ == 'main':
    tree = DegenerateTree()
    tree.insert(1)
    tree.insert(1)
    tree.insert(1)
    tree.insert(1)
    tree.insert(1)
            
            
            
            
        
    