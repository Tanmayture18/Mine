class BSTNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

newbst=BSTNode(None)

def traverse(rootnode):
    if rootnode is None:
        return rootnode
    traverse(rootnode.left)
    print(rootnode.data)
    traverse(rootnode.right)
 

def insert(rootnode,nodevalue):
    newnode=BSTNode(nodevalue)
    if rootnode.data is None:
        rootnode.data=nodevalue
    
    elif nodevalue<=rootnode.data:
        if rootnode.left is None:
            rootnode.left=newnode
        else:
            insert(rootnode.left,nodevalue)
    else:
        if rootnode.right is None:
            rootnode.right=newnode
        else:
            insert(rootnode.right,nodevalue)
            
def search(rootnode,nodevalue):
    
    if rootnode.data==nodevalue:
        print(True)
    elif nodevalue<rootnode.data:
        if rootnode.left.data==nodevalue:
            print(True)
        else:
            search(rootnode.left,nodevalue)
    else:
        if rootnode.right.data==nodevalue:
            print(True)
        else:
            search(rootnode.right,nodevalue)
            
# Delete method o(logN) O(logN)

# step 1 create minimum finding function for third classmethod
def minimum(rootnode):
    tempnode=rootnode
    while tempnode.left is not None:
        tempnode=tempnode.left
    return tempnode
    
# Step 2 Delte function
def delete(rootnode,nodevalue):
    if rootnode is None:
        return rootnode
        
    if nodevalue<rootnode.data:
        rootnode.left=delete(rootnode.left,nodevalue)
        
    elif nodevalue>rootnode.data:
        rootnode.right=delete(rootnode.right,nodevalue)
        
    
    else:
        # If node have one child
        if rootnode.left is None:
            temp=rootnode.right
            rootnode=None
            return temp
            
        if rootnode.right is None:
            temp=rootnode.left
            rootnode=None
            return temp
            
        # Tf node has two child
        temp=minimum(rootnode.right)  # We are finding successor ie smallest node in right subtree
        rootnode.data=temp.data
        rootnode.right=delete(rootnode.right,temp.data)
        
    return rootnode  
    

def deleteall(rootnode):   # O(1) O(1)
    rootnode.data=None
    rootnode.right=None
    rootnode.left=None
    
    
            

            
            
insert(newbst,10)
insert(newbst,5)
insert(newbst,20)
insert(newbst,2)
insert(newbst,30)

traverse(newbst)


print("______")
delete(newbst,30)
delete(newbst,2)

traverse(newbst)

deleteall(newbst)
traverse(newbst)
