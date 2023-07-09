# Creating doubly linkedlist


# Class for Node
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

#Class for doubly linkedlist
class DoublyLL:
    def __init__(self):
        self.head=None
        self.tail=None

    # Function for iterating
    def __iter__(self):
        tempnode=self.head
        while tempnode:
            yield tempnode
            tempnode=tempnode.next

    # Function for doubly linkedist   .O(1)
    def create(self,value):
        newnode=Node(value)  
        newnode.next=None
        newnode.prev=None
        self.head=newnode
        self.tail=newnode       


dl=DoublyLL()
dl.create(5)
print([node.value for node in dl])                