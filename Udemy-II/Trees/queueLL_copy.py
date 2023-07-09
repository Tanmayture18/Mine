# For level order traversal queue is needed henace we are going to create queue here

# we are going to create queue using linkedlits because we can dequeue using O(1) and using list this operation will neeed O(N)

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)    

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        tempnode=self.head
        while tempnode:
            yield tempnode
            tempnode=tempnode.next 

# Queue class
class Queue:
    def __init__(self):
        self.list=LinkedList()

    def __str__(self):
        l1=[str(i.value) for i in self.list]

        return "-" .join(l1)    

    def is_empty(self):
        if self.list.head is None:
            return True
        else: 
            return False

    def enqueue(self,value):
        newnode=Node(value)
        if self.list.head is None:
            self.list.head= newnode
            self.list.tail=newnode
        else:
            newnode.next=None
            self.list.tail.next=newnode
            self.list.tail=newnode

    def dequeue(self):
        if self.list.head is None:
            return 
        else:
            tempnode=self.list.head
            if self.list.head==self.list.tail:
                self.list.head=None
                self.list.tail=None
            else:
                
                self.list.head=self.list.head.next 
            return tempnode.value

    def peek(self): 
        if self.list.head is None:
            return 
        else:
            return self.list.head.value                   
