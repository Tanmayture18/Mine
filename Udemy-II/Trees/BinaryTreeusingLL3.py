# Searching in binary treee 
# We are going to use level order traversal since it uses queue Data structure and other uses stack data structure

from queueLL_copy import Queue

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


def search(rootnode,value):

    if rootnode is None:
        return "Empty Tree"
    else:
        queue=Queue()
        queue.enqueue(rootnode)

        while not (queue.is_empty()):
            root=queue.dequeue()

            if root.data==value:
                return  True

            if root.leftchild is not None:
                queue.enqueue(root.leftchild) 

            if root.rightchild is not None:
                queue.enqueue(root.rightchild)
        return False

print(search(newBT,'Hot'))   
print(search(newBT,'Tanmay'))             