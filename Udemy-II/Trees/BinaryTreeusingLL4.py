# Insert operation   O(N) O(N)
 
# We are going to use level order traversal for finding vacant place

from queueLL_copy import Queue
import queueLL


class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

newbt=TreeNode('Drinks')
hot=TreeNode('Hot')
cold=TreeNode('Cold')
newbt.leftchild=hot
newbt.rightchild=cold
tea=TreeNode('Tea')
cofe=TreeNode('Cofee')
hot.leftchild=tea
hot.rightchild=cofe







# Our Insert Function
def insert(rootnode,newnode):
    if not rootnode:
        rootnode=newnode
    else:
        queue=Queue()
        queue.enqueue(rootnode)

        while not(queue.is_empty()):
            root=queue.dequeue()

            if root.leftchild is not None:
                queue.enqueue(root.leftchild)
            else:
                root.leftchild=newnode  
                return "Root Inserted Successfully"  #VVIMP

            if root.rightchild is not None:
                queue.enqueue(root.rightchild)
            else:
                root.rightchild=newnode  
                return "Root inserted Successfullt"  #VVIMP other wise it will keep on inserting



def levelorder(rootnode):
    if not rootnode:
        return
    else:
        cusqueue=Queue()
        cusqueue.enqueue(rootnode)

        while not(cusqueue.is_empty()):
        
            root=cusqueue.dequeue()
            print(root.data) #  we areusing rootnode.value because in queue we are returning only node not its value
            
            if root.leftchild is not None:
                cusqueue.enqueue(root.leftchild)

            if root.rightchild is not None:
                cusqueue.enqueue(root.rightchild)

levelorder(newbt)

print('______________________')

biryani=TreeNode('Biryani') 
rice=TreeNode('Rice')
insert(newbt,biryani)
insert(newbt,rice)

levelorder(newbt)   # We can see that we have inserted node succeffully





