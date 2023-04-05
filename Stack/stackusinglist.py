# Creating stack class
class Stack:
    def __init__(self):
        self.list=[]

    # Function for printing elements of stack
    def __str__(self):
        
        values=[str(i) for i in self.list]
        return " ".join(values)
    
    # Is empty   O(1)
    def is_empty(self):
        if self.list==[]:
            return True
        else:
            return False 

    # Push     O(1)
    def push(self,value):
        self.list.append(value)   

    # Pop    O(1)
    def pop(self):
        if self.is_empty():
            return "Empty Stack"
        else:
            return self.list.pop()  

    # Peak   O(1)
    def peek(self):
        if self.is_empty():
            return "Stack EMpty"         
        else:
            return self.list[-1]
        
    def delete(Self):
        Self.list=None    




stack=Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.is_empty())
print(stack.pop())
print(stack)
print(stack.peek())
stack.delete()
print(stack)
