class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        tempnode=self.head
        while tempnode:
            yield tempnode
            if tempnode.next==self.head:
                break
            tempnode=tempnode.next 

    # Function for creation 
    def create(self,value):
        newnode=Node(value)
        newnode.next=newnode
        newnode.prev=newnode
        self.head=newnode
        self.tail=newnode

    # Function for insertion   O(N)
    def insert(self,value,location):
        if self.head is None:
            print("Node cannot be inserted")
        else:
            newnode=Node(value)
            # Inserting at begining
            if location==0:
                newnode.prev=self.tail
                newnode.next=self.head
                self.head.prev=newnode
                self.tail.next=newnode
                self.head=newnode

            # Inserting at end
            elif location==1:
                newnode.next=self.head
                newnode.prev=self.tail
                self.tail.next=newnode
                self.head.prev=newnode
                self.tail=newnode

            # Inserting at an arbitary position
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

    # TRaversing     O(N)
    def traverse(self):
        if self.head is None:
            print("Empty LinkedList")
        else:
            tempnode=self.head
            while tempnode:
                print(tempnode.value)
                if tempnode==self.tail:
                    break
                tempnode=tempnode.next   

    # Reverse traverse   O(N)
    def reverse(self):
        if self.head is None:
            print("Empty LinkedList")
        else:
            tempnode=self.tail
            while tempnode:
                print(tempnode.value)
                if tempnode==self.head:
                    break
                tempnode=tempnode.prev

    # Searching   O(N)
    def search(self,value):
        if self.head is None:
            print("Empty LinkedList")
        else:
            tempnode=self.head
            while tempnode:
                if tempnode.value==value:
                    return True
                if tempnode==self.tail:
                    break
                tempnode=tempnode.next
            return False
            

 

    
cl=CircularDoublyLinkedList()
cl.create(10)
cl.insert(100,1)
cl.insert(200,0)
cl.insert(1000,-1)
print([node.value for node in cl])
cl.traverse()
cl.reverse()
print(cl.search(10))
print(cl.search(-100))