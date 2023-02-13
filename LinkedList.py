class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    # Reprsenting Function
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            
    # Inserting function
    def insert(self,value,location):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            # Begining
            if location==0:
                newnode.next=self.head
                self.head=newnode
            
            # Ending
            elif location==1:
                newnode.next=None
                self.tail.next=newnode
                self.tail=newnode
            
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=newnode
                newnode.next=nextnode
                
    # Traversing function 
    def traverse(self):
        tempnode=self.head
        while tempnode is not None:
            print(tempnode.value)
            tempnode=tempnode.next
    
    # Searching function
    def search(self,value):
        tempnode=self.head
        
        while tempnode is not None:
            if tempnode.value==value:
                return 'Element Exists'
            
            tempnode=tempnode.next    
        return 'Element Doesn"t Exists' 
        
        
    # Deletion function
    def delete(self,location):
        
        if self.head is None:
            print("Empty LinkedLIst")
        else:
            # Deletion from begining
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
            
            # Deletion from end
            elif location==1:
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
            
            # Deletion from arbitary position
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next.next
                tempnode.next=nextnode
                
            
            
                
                
    




l=LinkedList()
l.insert('Tanmay',0)
l.insert('Ture',1)
l.insert('Tans',0)
l.insert('TANMAY',1)
l.insert('SAHIL',2)
print([i.value for i in l])
print(l.search('TANMAY'))
print(l.search('dipak'))


l.delete(0)
l.delete(1)
l.insert(10,0)
l.insert(20,0)
l.delete(2)
print([i.value for i in l])
