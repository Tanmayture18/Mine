class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        tempnode=self.head
        while tempnode:
            yield tempnode
            tempnode=tempnode.next 

    def create(self,value):
        newnode=Node(value)
        newnode.next=None
        newnode.prev=None
        self.head=newnode
        self.tail=newnode

    def insert(self,value,location):
        if self.head is None:
            print("Node cannot be inserted")
        else:
            newnode=Node(value)
            if location==0:
                newnode.prev=None
                newnode.next=self.head
                self.head.prev=newnode
                self.head=newnode
            elif location==-1:
                newnode.next=None
                newnode.prev=self.tail
                self.tail.next=newnode
                self.tail=newnode
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                newnode.next=tempnode.next
                newnode.prev=tempnode
                tempnode.next.prev=newnode
                tempnode.next=newnode
                        
    
    # Traversing linkedlist      O(N)
    def traverse(self):
        if self.head is None:
            print("Empty Doubly LinkedList")
        tempnode=self.head
        while tempnode:
            print(tempnode.value)
            tempnode=tempnode.next

    # Reverse Traverse of Doubly LinkedlIst    O(N)
    def reverse(self):
        if self.head is None:
            print("Empty LinkedList")
        else:
            tempnode=self.tail
            while tempnode:
                print(tempnode.value)
                tempnode=tempnode.prev




dl=DoublyLL()
dl.create(5)
dl.insert(10,0)
dl.insert(20,-1)
dl.insert(100,1)
print([node.value for node in dl])   
dl.traverse()     
print('___________________')  
dl.reverse()         