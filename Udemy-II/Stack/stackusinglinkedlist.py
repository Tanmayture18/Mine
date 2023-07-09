class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def __iter__(self):
        tempnode=self.head
        while tempnode:
            yield tempnode
            tempnode=tempnode.next    


class Stack:
    def __init__(self):
        self.ll=LinkedList()

    def __str__(self):
        values=[str(i.value) for i in self.ll]   
        return '\n'.join(values) 
    
    def is_empty(self):    #O(1)
        if self.ll.head is None:
            return True
        else:
            return False
        
    def push(self,value):
        newnode=Node(value)
        newnode.next=self.ll.head
        self.ll.head=newnode   

    def pop(self):
        if self.is_empty():
            return 'Empty Stack'
        tempnode=self.ll.head
        self.ll.head=self.ll.head.next
        return tempnode.value
    
    def peek(self):
        if self.is_empty():
            return "Empty Linkedlist"
        else:
            return self.ll.head.value
        
    def delete(self):
        self.ll.head=None    
         

    
stack=Stack()
print(stack)  
print(stack.is_empty())  
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print('----------')
print(stack.pop())
print('----------')
print(stack)
print(stack.peek())
stack.delete()
print(stack)
