# Traversals 

#1) Pre order traversal    (root-->Left subtree-->right subtree)

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None


newBT=TreeNode('Drinks')
# Adding childs 
Hot=TreeNode('Hot')
Cold=TreeNode('Cold')

Tea=TreeNode('Tea')
Cofe=TreeNode('Cofee')
Hot.leftchild=Tea
Hot.rightchild=Cofe


newBT.leftchild=Hot
newBT.rightchild=Cold

# Pre order traversal function   time O(N),space O(N)
def preorder(rootnode):
    if not rootnode:      # If root node is None
        return 
    print(rootnode.data)
    preorder(rootnode.leftchild)
    preorder(rootnode.rightchild)

preorder(newBT)

print("____________")
# 2) In order traversal   left subtree-->rootnode-->right subtree     time: O(N) space O(N)
def inorder(rootnode):
    if not rootnode:
        return 
    inorder(rootnode.leftchild)
    print(rootnode.data)
    inorder(rootnode.rightchild) 

inorder(newBT)

print("____________")
# 3) Post order traversal     left subtree-->right subtree-->rootnode

def postorder(rootnode):
    if not rootnode:
        return 
    postorder(rootnode.leftchild)
    postorder(rootnode.rightchild)
    print(rootnode.data)

postorder(newBT)
print("____________")


# 4) Inorder Trvaersal   O(N)  O(N)

import queueLL as queue

def levelorder(rootnode):
    if not rootnode:
        return
    else:
        cusqueue=queue.Queue()
        cusqueue.enqueue(rootnode)

        while not(cusqueue.is_empty()):
            root=cusqueue.dequeue()
            print(root.value.data) #  we areusing rootnode.value because in queue we are returning only node not its value
            
            if root.value.leftchild is not None:
                cusqueue.enqueue(root.value.leftchild)

            if root.value.rightchild is not None:
                cusqueue.enqueue(root.value.rightchild)

levelorder(newBT)


        





