class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__(self):
        tempnode=self.head
        while tempnode:
            yield tempnode
            tempnode=tempnode.next
    
class Queue:
    def __init__(self):
        self.list=LinkedList()
    
    def __str__(self):
        values=[str(x.value) for x in self.list]
        return " ".join(values)
        
    def is_empty(self):   #O(1)
        if self.list.head is None:
            return True
        else:
            return False
    
    def enqueue(self,value):   #O(1)
        newnode=Node(value)
        if self.list.head is None:
            self.list.head=newnode
            self.list.tail=newnode
        else:
            newnode.next=None
            self.list.tail.next=newnode
            self.list.tail=newnode
            
    def dequeue(self):    #O(1)
        if self.is_empty():
            return "Empty Queue"
        else:
            tempnode=self.list.head
            self.list.head=self.list.head.next
            return tempnode.value
            
    def peek(self):    #O(1)
        if self.is_empty():
            return "Empty"
        else:
            return self.list.head.value
            
    def delete(self):  #O(1)
        self.list.head=None
        self.list.tail=None
        
        

queue=Queue()
print(queue)
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
print(queue.is_empty())
print(queue.dequeue())
print(queue)
print(queue.peek())
queue.delete()
print(queue)


        