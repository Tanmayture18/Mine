# Search 
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

insert(newbst,10)
insert(newbst,5)
insert(newbst,20)
insert(newbst,30)

def inorder(rootnode):
    if not rootnode:
        return
    else:
        inorder(rootnode.left)
        print(rootnode.data)
        inorder(rootnode.right)
inorder(newbst)   

def search(rootnode,nodevalue):  # O(logN) O(logN)
    if rootnode.data==nodevalue:
        return True
    elif nodevalue<rootnode.data:
        if rootnode.left.data==nodevalue:
            return True
        else:
            search(rootnode.left,nodevalue)
    else:
        if rootnode.right.data==nodevalue:
            return True
        else:
            search(rootnode.right,nodevalue)
            
    
    
print(search(newbst,20))
print(search(newbst,5))
    


