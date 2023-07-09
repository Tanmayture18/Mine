class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class CLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def circular(self,value):
        newnode=Node(value)
        newnode.next=newnode
        self.head=newnode
        self.tail=newnode

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

    # Function for traversing
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
                     


cl=CLinkedlist()
cl.circular(5)
cl.insert(10,0)
cl.insert(15,1)
cl.insert(20,2)
print([i.value for i in cl]) 
cl.traverse() 

print(cl.search(10))
print(cl.search('Tans'))
