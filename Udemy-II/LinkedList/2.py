#2) Create Node clas
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

#1) Create linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    # Function for printing elements of linkedlist
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next     

    # Create insertion function
    def insert(self,value,location):

        newnode=Node(value)

        # If linked list is empty
        if self.head is None:
            self.head=newnode
            self.tail=newnode

        else:
            # Insertion at begining
            if location==0:
                newnode.next=self.head
                self.head=newnode

            # Insertion at end
            elif location==1:
                newnode.next=None
                self.tail.next=newnode
                self.tail=newnode

            # Insertion at arbitary position
            else:
                tempnode=self.head
                index=0

                while index<location-1:
                    tempnode=tempnode.next
                    index+=1

                nextnode=tempnode.next
                tempnode.next=newnode
                newnode.next=nextnode

l=LinkedList()
l.insert('Tans',0) 
l.insert('Ture',1)  
l.insert('Tanmay',0) 
l.insert('ture',0)
l.insert('TURE',2)
print([node.value for node in l]) 

