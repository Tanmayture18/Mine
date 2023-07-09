class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode
    
    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head
    
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None



class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        

newbt=Treenode('Drinks')
hot=Treenode('hot')
cold=Treenode('cold')
newbt.left=hot
newbt.right=cold
tea=Treenode('tea')
coffe=Treenode('coffe')
hot.left=tea
hot.right=coffe


def levelorder(rootnode):
    
    if rootnode is None:
        return 
    else:
        queue=Queue()
        queue.enqueue(rootnode)
        
        while not(queue.isEmpty()):
            root=queue.dequeue()
            
            print(root.value.data)
            
            if root.value.left is not None:
                queue.enqueue(root.value.left)
            
            if root.value.right is not None:
                queue.enqueue(root.value.right)


def search(rootnode,value):
    if not rootnode:
        return 
    else:
        queue=Queue()
        queue.enqueue(rootnode)
        
        while not queue.isEmpty():
            root=queue.dequeue()
            
            if root.value.data==value:
                return True
                
            if root.value.left is not None:
                queue.enqueue(root.value.left)
            
            if root.value.right is not None:
                queue.enqueue(root.value.right)
        return False        

def insert(rootnode,treenode):
    if not rootnode:
        rootnode=treenode
    else:
        queue=Queue()
        queue.enqueue(rootnode)
        
        while not queue.isEmpty():
            root=queue.dequeue()
            
            if root.value.left is not None:
                queue.enqueue(root.value.left)
            else:
                root.value.left=treenode
                return 'Succees'
            if root.value.right is not None:
                queue.enqueue(root.value.right)
            else:
                root.value.right=treenode
                return 'Success'

insert(newbt,Treenode('Coke'))
insert(newbt,Treenode('Limca'))

# levelorder(newbt)



# Delete Method O(N)  O(N)

# We will use 3 functions for deleting a particular node,
# Idea find node swap it with deepest node delete deepest node

# 1 st  function (get deepest node)

def getdeepestnode(treenode):
    
    if not treenode:
        return 
    else:
        queue=Queue()
        queue.enqueue(treenode)
        
        while not queue.isEmpty():
            root=queue.dequeue()
            
            if root.value.left is not None:
                queue.enqueue(root.value.left)
            
            if root.value.right is not None:
                queue.enqueue(root.value.right)
        
        deepnode=root.value
        return deepnode
        
a=getdeepestnode(newbt)
print(a.data)   # our function successfuly identifies correct answe limca
print("________________")


# 2nd function delete deepest node

def deletedeepest(rootnode,dnode):
    if not rootnode:
        return 
    else:
        queue=Queue()
        queue.enqueue(rootnode)
        
        while not queue.isEmpty():
            root=queue.dequeue()
            
            if root.value is dnode:
                root.value=None
                return
            
            if root.value.left:
                if root.value.left is dnode:
                    root.value.left=None
                    return 
                else:
                    queue.enqueue(root.value.left)
                    
            if root.value.right:
                if root.value.right is dnode:
                    root.value.right=None
                    return
                else:
                    queue.enqueue(root.value.right)

# deletedeepest(newbt,a)      

# levelorder(newbt) # we can see that our method works fine and delete deepest node limca

# 3rd method 
def deletenode(rootnode,nodevalue):
    if not rootnode:
        return 
    else:
        queue=Queue()
        queue.enqueue(rootnode)
        
        while not queue.isEmpty():
            root=queue.dequeue()
            
            if root.value.data==nodevalue:
                dnode=getdeepestnode(rootnode)
                root.value.data=dnode.data
                deletedeepest(rootnode,dnode)
                
                return 'Success'
            
            if root.value.left is not None:
                queue.enqueue(root.value.left)
            
            if root.value.right is not None:
                queue.enqueue(root.value.right)

deletenode(newbt,'hot')
levelorder(newbt)

print("____________________")

# We can see that we deleteed node tea and replaced it with deepest node which was Limca

def deleteentire(rootnode):
    if rootnode is None:
        return 
    else:
        rootnode.data=None
        rootnode.left=None
        rootnode.right=None

deleteentire(newbt) 
levelorder(newbt)
# We successfully deleted binary tree




                    
    

    
    
    
    
    
    
    
    