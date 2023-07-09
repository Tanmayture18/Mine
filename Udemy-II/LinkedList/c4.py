# Class for node
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

#Class for circular linked List
class CLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    
    # Function for creating circular linkedlist
    def circular(self,value):
        newnode=Node(value)
        newnode.next=newnode
        self.head=newnode
        self.tail=newnode

    # Iteration function
    def __iter__(self):
        tempnode=self.head
        while tempnode:
            yield tempnode
            if tempnode.next==self.head:
                break
            tempnode=tempnode.next  

    # Insertion function   O(N)
    def insert(self,value,location):
        if self.head is None:
            return "Empty LinkedList"

        else:
            newnode=Node(value)
            #Insertion at begining
            if location==0:
                newnode.next=self.head
                self.head=newnode
                self.tail.next=newnode

            # Insertion at end
            elif location==1:
                newnode.next=self.tail.next
                self.tail.next=newnode
                self.tail=newnode

            # Insertion at end
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=newnode
                newnode.next=nextnode   

    # Function for traversing    O(N)
    def traverse(self):
        if self.head is None:
            print("Empty Linked LIst")
        else:
            tempnode=self.head
            while tempnode is not None:
                print(tempnode.value)
                tempnode=tempnode.next
                if tempnode==self.tail.next  :
                    break   

    # Function for search O(N)
    def search(self,nodevalue):
        if self.head is None:
            return "Empty LinkedList"
        else:
            tempnode=self.head
            while tempnode:
                if tempnode.value==nodevalue:
                    return "Element exists in linkedlist"
                tempnode=tempnode.next
                if tempnode==self.tail.next:
                    return 'Element doesnot exists in linkedlist'
                    break                                          
                     
    # Function for deleting node from CLL O(N)
    def delete(self,location):
        if self.head is None:
            print("Empty linked list")
        else:
            # Deleting first node
            if location==0:

                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head    

            # Deleting last node
            elif location==1:

                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    tempnode=self.head
                    while tempnode is not None:
                        if tempnode.next==self.tail:
                            break
                        tempnode=tempnode.next
                    tempnode.next=self.head
                    self.tail=tempnode   

            # Deleting node from an arbitary position
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=nextnode.next    

    # Deleting entire CLL
    def deleteall(self):
        self.head=None
        self.tail.next=None
        self.tail=None
            




cl=CLinkedlist()
cl.circular(5)
cl.insert(10,0)
cl.insert(15,1)
cl.insert(20,2)
print([i.value for i in cl]) 
cl.traverse() 

print(cl.search(10))
print(cl.search('Tans'))
print([i.value for i in cl]) 
cl.delete(0)
print([i.value for i in cl]) 
cl.delete(1)
print([i.value for i in cl]) 
cl.insert(0,0)
cl.insert(10,0)
print([i.value for i in cl]) 
cl.delete(2)
print([i.value for i in cl]) 
cl.deleteall()
print([node.value for node in cl])
