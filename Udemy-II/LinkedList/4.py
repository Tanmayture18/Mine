#2)Create Node class
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

# 1) Create Linked List class
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

    # create insertion function
    def insert(self,value,position):
        newnode=Node(value)

        if self.head is None:
            self.head=newnode
            self.tail=newnode
       
        else:
            # Insert at begining
            if position==0:
                newnode.next=self.head
                self.head=newnode

            # Insert at end
            elif position==1:
                newnode.next=None
                self.tail.next=newnode
                self.tail=newnode

            # Insert at arbitary position
            else:
                tempnode=self.head
                index=0
                while index<position-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=newnode
                newnode.next=nextnode  


    # Function for traversing
    def traverse(self):  
        if self.head is None:
            print("Empty LinkedList")
        tempnode=self.head
        while tempnode is not None:
            print(tempnode.value)
            tempnode=tempnode.next              


    # Function for searching element
    def search(self,value):
        if self.head is None:
            print("Empty LinkedList")
        tempnode=self.head
        while tempnode is not None:
            if tempnode.value==value:
                return True
            tempnode=tempnode.next
        return False


    # Function For deletion   O(N)
    def delete(self,location):
        # IF linkedlist is empty
        if self.head is None:
            print("Empty LinkedList")
        else:
            # Deletion from begining
            if  location==0:
                # If only one element is present in linkedlist
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next

            # Deleting from end
            elif location==1:
                # If only one element is present in linkedlist
                if self.head==self.tail:
                    self.head=None
                    self.tail=None  
                else:
                    tempnode=self.head
                    while tempnode is not None:
                        if tempnode.next==self.tail:
                            break
                        tempnode=tempnode.next
                    tempnode.next=None
                    self.tail=tempnode

            # Deleting from an arbitary position
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1

                nextnode=tempnode.next
                tempnode.next=nextnode.next  
    
    # Deleting entire linkedlist    O(1)
    def deletelist(self):
        if self.head is None:
            print("Empty Linked List")   

        else:
            self.head=None
            self.tail=None               



l=LinkedList()
l.insert(10,0)
l.insert(11,1)
l.insert(9,0)
l.insert(12,2)
# print([node.value for node in l])   
# print("____________________________") 
# l.traverse() 
# print("_____________________________")  
# print(l.search(9))     
# print(l.search('Tanmay')) 
print("____________________________")
print([node.value for node in l])   
l.delete(0)
print([node.value for node in l]) 
l.delete(1)
print([node.value for node in l])    
l.insert(13,1)
l.insert(14,1)
print([node.value for node in l])  
l.delete(2)
print([node.value for node in l])   

l.deletelist()
print([node.value for node in l])   




