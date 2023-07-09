# Ceating BST

class BSTNode:   # TIme O(1) space O(1)
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

newbst=BSTNode(None)


# Insert Method

def insert(rootnode,nodevalue):  # Time O(logN) space 0(logN)
    
    if rootnode.data==None: # If rootnode is empty
        rootnode.data=nodevalue
    
    elif nodevalue<=rootnode.data :  # IF nodevalue less than rootnode
        if rootnode.left is None:
            rootnode.left=BSTNode(nodevalue)
        else:
            insert(rootnode.left,nodevalue)
    
    else:                            # If nodevalue greater than rightnode
        if rootnode.right is None:
            rootnode.right=BSTNode(nodevalue)
        else:
            insert(rootnode.right,nodevalue) 
    return 'Success'

print(insert(newbst,10))
print(insert(newbst,5))
print(newbst.left.data)
