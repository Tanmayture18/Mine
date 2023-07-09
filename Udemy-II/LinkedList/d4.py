# Node class
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

# Linkedlist class
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    # Function for iterating
    def __iter__(self):
        tempnode=self.head
        while tempnode:
            yield tempnode
            tempnode=tempnode.next

    # Function for creating doubly linkedlist
    def create(self,value):
        newnode=Node(value)
        newnode.next=None
        newnode.prev=None
        self.head=newnode
        self.tail=newnode

    # Function for insertion   O(N)
    def insert(self,value,location):
        if self.head is None:
            print("The node can not be inserted")
        else:
            newnode=Node(value)
            # Inserting at begining
            if location==0:
                newnode.next=self.head
                newnode.prev=None
                self.head.prev=newnode
                self.head=newnode

            # Inserting at end
            elif location==1:
                newnode.next=None
                newnode.prev=self.tail
                self.tail.next=newnode
                self.tail=newnode

            # Inserting at arbitary position
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

    # Function for traversing   O(N)
    def traverse(self):
        if self.head is None:
            print("Empty Linked List")
        tempnode=self.head
        while tempnode:
            print(tempnode.value)
            tempnode=tempnode.next

    # Function for reversing   O(N)
    def reverse(self):
        if  self.head is None:
            print("Empty Linkedlist")
        tempnode=self.tail
        while tempnode:
            print(tempnode.value)
            tempnode=tempnode.prev  

    # Function for searching O(N)
    def search(self,value):
        if self.head is None:
            print('Empty Linked List')
        tempnode=self.head
        while tempnode:
            if tempnode.value==value:
                return True
            tempnode=tempnode.next
        return False   
    
    # Deletion in doubly linked list    O(N)
    def delete(self,location):
        if self.head is None:
            print("Empty LinkedList")
        else:
            # Deleting first node
            if location==0:
                if self.head==self.tail:    # If length of linkedlist is 1
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None  

            # Deleting last node
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None

            # Deleting node at an arbitary position
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                tempnode.next=tempnode.next.next
                tempnode.next.prev=tempnode 

    # Deletion of entire linked list
    def delall(self):
        if self.head is None:
            print('Empty linked List')
        else:
            tempnode=self.head
            while tempnode:
                tempnode.prev=None
                tempnode=tempnode.next
            self.head=None
            self.tail=None



                     
                              

        

dl=DoublyLinkedList()
dl.create(10)
dl.insert(5,0)
dl.insert(15,1)
dl.insert(100,-1)     # Since we are using 1 to insert at end hence if we want to insert at arbitary postion 1 we can use -1
print([node.value for node in dl])
dl.traverse()
print('- - - - -')
dl.reverse()
print(dl.search(5))
print(dl.search(-1))
dl.delete(0)
dl.delete(-1)
dl.delete(1)

print([node.value for node in dl])
dl.delall()
print([node.value for node in dl])